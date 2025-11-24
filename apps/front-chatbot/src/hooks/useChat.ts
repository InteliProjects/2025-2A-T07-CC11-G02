import { useState, useCallback, useRef, useEffect } from 'react';
import { chatApi, checkConnectionStatus } from '@/services/api';
import type { Message, ChatRequest, ChatStatus } from '@/types/chat';

export const useChat = (externalId?: string) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [chatStatus, setChatStatus] = useState<ChatStatus>({
    isOnline: false,
    connectionStatus: 'disconnected',
    retryCount: 0,
  });
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const connectionCheckInterval = useRef<number | null>(null);

  // Auto-scroll para a última mensagem
  const scrollToBottom = useCallback(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, []);

  // Verificar status de conexão
  const checkConnection = useCallback(async () => {
    // Não verificar conexão durante carregamento para evitar conflitos
    if (isLoading) {
      return;
    }
    
    try {
      const status = await checkConnectionStatus();
      setChatStatus(prev => ({
        ...prev,
        connectionStatus: status,
        isOnline: status === 'connected',
        lastError: status === 'error' ? 'Erro de conexão' : undefined,
      }));
    } catch (err) {
      setChatStatus(prev => ({
        ...prev,
        connectionStatus: 'error',
        isOnline: false,
        lastError: 'Falha ao verificar conexão',
      }));
    }
  }, [isLoading]);

  // Iniciar verificação periódica de conexão
  const startConnectionCheck = useCallback(() => {
    if (connectionCheckInterval.current) {
      clearInterval(connectionCheckInterval.current);
    }
    
    checkConnection(); // Verificação inicial
    
    connectionCheckInterval.current = setInterval(checkConnection, 30000); // A cada 30 segundos
  }, [checkConnection]);

  // Parar verificação de conexão
  const stopConnectionCheck = useCallback(() => {
    if (connectionCheckInterval.current) {
      clearInterval(connectionCheckInterval.current);
      connectionCheckInterval.current = null;
    }
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages, scrollToBottom]);

  // Iniciar verificação de conexão ao montar o componente
  useEffect(() => {
    startConnectionCheck();
    return () => stopConnectionCheck();
  }, [startConnectionCheck, stopConnectionCheck]);

  // Adicionar mensagem de boas-vindas inicial (apenas visual, não enviada para backend)
  useEffect(() => {
    const welcomeMessage: Message = {
      id: 'welcome',
      text: 'Oi! Tudo bem? Aqui é do time Curadobia ✨ Como posso te ajudar hoje?',
      isUser: false,
      timestamp: new Date(),
      isWelcomeMessage: true, // Marcar como mensagem de boas-vindas
    };
    setMessages([welcomeMessage]);
  }, []);

  const sendMessage = useCallback(async (text: string) => {
    if (!text.trim() || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      text: text.trim(),
      isUser: true,
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    setError(null);

    try {
      const request: ChatRequest = {
        text: text.trim(),
        external_id: externalId,
      };

      const response = await chatApi.sendMessage(request);
      
      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: response.response,
        isUser: false,
        timestamp: new Date(),
        intent: response.intent,
        metadata: response.metadata,
      };

      setMessages(prev => [...prev, botMessage]);
      
      // Reset retry count em caso de sucesso
      setChatStatus(prev => ({ ...prev, retryCount: 0 }));
      
    } catch (err) {
      console.error('Erro ao enviar mensagem:', err);
      
      let errorMessage = 'Erro ao enviar mensagem';
      let userFriendlyMessage = 'Desculpe, ocorreu um erro. Tente novamente em alguns instantes.';
      let isNetworkError = false;
      let shouldRetry = false;
      
      if (err instanceof Error) {
        errorMessage = err.message;
        
        // Tratamento específico para diferentes tipos de erro
        if ((err as any).isTimeout) {
          userFriendlyMessage = 'O modelo está sendo carregado pela primeira vez e pode demorar até 10 minutos. Aguarde um pouco mais ou tente novamente.';
          shouldRetry = true;
        } else if ((err as any).isNetworkError) {
          userFriendlyMessage = 'Erro de conexão. Verifique se o servidor está rodando.';
          isNetworkError = true;
        } else if ((err as any).isServerError) {
          userFriendlyMessage = 'Erro interno do servidor. Tente novamente em alguns instantes.';
          shouldRetry = true;
        } else if ((err as any).isNotFound) {
          userFriendlyMessage = 'Serviço não encontrado. Verifique se o servidor está configurado corretamente.';
        } else if ((err as any).isBadRequest) {
          userFriendlyMessage = 'Requisição inválida. Tente reformular sua mensagem.';
        } else if (err.message.includes('500')) {
          userFriendlyMessage = 'Erro interno do servidor. Tente novamente em alguns instantes.';
          shouldRetry = true;
        } else if (err.message.includes('timeout')) {
          userFriendlyMessage = 'Timeout na requisição. O modelo pode estar carregando pela primeira vez. Aguarde mais um pouco.';
          shouldRetry = true;
        }
      }
      
      setError(errorMessage);
      
      // Atualizar status de conexão em caso de erro de rede
      if (isNetworkError) {
        setChatStatus(prev => ({
          ...prev,
          connectionStatus: 'disconnected',
          isOnline: false,
          lastError: errorMessage,
          retryCount: prev.retryCount + 1,
        }));
      } else if (shouldRetry) {
        setChatStatus(prev => ({
          ...prev,
          connectionStatus: 'error',
          isOnline: false,
          lastError: errorMessage,
          retryCount: prev.retryCount + 1,
        }));
      }
      
      const errorBotMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: userFriendlyMessage,
        isUser: false,
        timestamp: new Date(),
        isError: true,
        metadata: {
          fallback: {
            type: 'unknown_intent',
            reason: 'error'
          }
        }
      };

      setMessages(prev => [...prev, errorBotMessage]);
    } finally {
      setIsLoading(false);
    }
  }, [isLoading, externalId, chatStatus.isOnline, checkConnection]);

  const clearMessages = useCallback(() => {
    setMessages([]);
    setError(null);
  }, []);

  return {
    messages,
    isLoading,
    error,
    chatStatus,
    sendMessage,
    clearMessages,
    checkConnection,
    messagesEndRef,
  };
};
