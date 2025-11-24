import axios, { AxiosError } from 'axios';
import type { ChatRequest, ChatResponse, User, ConnectionStatus } from '@/types/chat';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// Configuração de timeout baseada no tipo de operação
const TIMEOUTS = {
  HEALTH_CHECK: 5000,
  CHAT: 600000, // 10 minutos para chat (modelo pode demorar muito para carregar na primeira vez)
  USER_OPERATIONS: 10000,
} as const;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    'ngrok-skip-browser-warning': 'true',
  },
});

// Interceptor para configurar timeout baseado na operação
api.interceptors.request.use((config) => {
  if (config.url?.includes('/healthz')) {
    config.timeout = TIMEOUTS.HEALTH_CHECK;
  } else if (config.url?.includes('/chat')) {
    config.timeout = TIMEOUTS.CHAT;
  } else {
    config.timeout = TIMEOUTS.USER_OPERATIONS;
  }
  return config;
});

// Request interceptor para adicionar logs
api.interceptors.request.use(
  (config) => {
    console.log(`[API] ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error('[API] Request error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor para tratamento de erros
api.interceptors.response.use(
  (response) => {
    console.log(`[API] Response:`, response.status, response.data);
    return response;
  },
  (error: AxiosError) => {
    console.error('[API] Response error:', error.response?.data || error.message);
    
    // Tratamento específico de erros
    if (error.code === 'ECONNABORTED') {
      const timeoutError = new Error('Request timeout');
      (timeoutError as any).isTimeout = true;
      (timeoutError as any).code = error.code;
      return Promise.reject(timeoutError);
    }
    
    if (error.code === 'ERR_NETWORK' || error.code === 'ERR_INTERNET_DISCONNECTED') {
      const networkError = new Error('Network error');
      (networkError as any).isNetworkError = true;
      (networkError as any).code = error.code;
      return Promise.reject(networkError);
    }
    
    // Tratamento de erros HTTP específicos
    if (error.response) {
      const status = error.response.status;
      const customError = new Error(`HTTP ${status}: ${(error.response.data as any)?.detail || error.message}`);
      (customError as any).status = status;
      (customError as any).response = error.response.data;
      
      if (status >= 500) {
        (customError as any).isServerError = true;
      } else if (status === 404) {
        (customError as any).isNotFound = true;
      } else if (status === 400) {
        (customError as any).isBadRequest = true;
      }
      
      return Promise.reject(customError);
    }
    
    return Promise.reject(error);
  }
);

// Função para verificar status de conexão
export const checkConnectionStatus = async (): Promise<ConnectionStatus> => {
  try {
    const response = await api.get('/healthz', { timeout: TIMEOUTS.HEALTH_CHECK });
    return response.status === 200 ? 'connected' : 'error';
  } catch (error) {
    if (error instanceof Error) {
      if ((error as any).isTimeout) return 'disconnected';
      if ((error as any).isNetworkError) return 'disconnected';
      if ((error as any).isServerError) return 'error';
    }
    return 'error';
  }
};

// Função para retry com backoff exponencial
export const retryWithBackoff = async <T>(
  fn: () => Promise<T>,
  maxRetries: number = 3,
  baseDelay: number = 1000
): Promise<T> => {
  let lastError: Error;
  
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;
      
      if (attempt === maxRetries) {
        throw lastError;
      }
      
      const delay = baseDelay * Math.pow(2, attempt);
      console.log(`[API] Retry attempt ${attempt + 1}/${maxRetries} in ${delay}ms`);
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
  
  throw lastError!;
};

export const chatApi = {
  // Enviar mensagem para o chatbot com retry automático
  sendMessage: async (request: ChatRequest): Promise<ChatResponse> => {
    return retryWithBackoff(async () => {
      const response = await api.post<ChatResponse>('/chat', request);
      return response.data;
    }, 3, 5000); // 3 retries com delay de 5s (para dar tempo do modelo carregar)
  },

  // Verificar saúde da API
  healthCheck: async (): Promise<{ status: string; endpoints: any }> => {
    const response = await api.get('/healthz');
    return response.data;
  },

  // Verificar se o serviço está disponível
  isAvailable: async (): Promise<boolean> => {
    try {
      await api.get('/healthz', { timeout: TIMEOUTS.HEALTH_CHECK });
      return true;
    } catch {
      return false;
    }
  },
};

export const userApi = {
  // Criar usuário
  createUser: async (userData: Partial<User>): Promise<User> => {
    return retryWithBackoff(async () => {
      const response = await api.post<User>('/users', userData);
      return response.data;
    });
  },

  // Buscar usuário por ID
  getUserById: async (userId: number): Promise<User> => {
    return retryWithBackoff(async () => {
      const response = await api.get<User>(`/users/${userId}`);
      return response.data;
    });
  },

  // Buscar usuário por external_id
  getUserByExternalId: async (externalId: string): Promise<User> => {
    return retryWithBackoff(async () => {
      const response = await api.get<User>(`/users/by-external/${externalId}`);
      return response.data;
    });
  },

  // Listar usuários
  listUsers: async (limit = 50, offset = 0): Promise<User[]> => {
    return retryWithBackoff(async () => {
      const response = await api.get<User[]>(`/users?limit=${limit}&offset=${offset}`);
      return response.data;
    });
  },

  // Atualizar usuário
  updateUser: async (userId: number, userData: Partial<User>): Promise<User> => {
    return retryWithBackoff(async () => {
      const response = await api.patch<User>(`/users/${userId}`, userData);
      return response.data;
    });
  },

  // Deletar usuário
  deleteUser: async (userId: number): Promise<{ deleted: boolean }> => {
    return retryWithBackoff(async () => {
      const response = await api.delete(`/users/${userId}`);
      return response.data;
    });
  },
};

export default api;
