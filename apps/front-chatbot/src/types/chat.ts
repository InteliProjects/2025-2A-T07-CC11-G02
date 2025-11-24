export interface Message {
  id: string;
  text: string;
  isUser: boolean;
  timestamp: Date;
  intent?: string;
  metadata?: ChatResponse['metadata'];
  isError?: boolean;
  isTyping?: boolean;
  isWelcomeMessage?: boolean;
}

export type ConnectionStatus = 'connected' | 'connecting' | 'disconnected' | 'error';

export interface ChatStatus {
  isOnline: boolean;
  connectionStatus: ConnectionStatus;
  lastError?: string;
  retryCount: number;
}

export interface ChatRequest {
  text: string;
  external_id?: string;
}

export interface ChatResponse {
  response: string;
  intent?: string;
  metadata?: {
    classifier?: {
      predicted_label?: string;
      predicted_class?: number;
      score?: number;
    };
    rag?: {
      used: boolean;
      question?: string;
      contexts?: Array<{
        id?: string;
        type?: string;
        text?: string;
        score?: number;
      }>;
      context_count?: number;
      max_score?: number;
      score_threshold?: number;
      scores?: number[];
      insufficient_context?: boolean;
      error?: string;
      fallback_reason?: string;
    };
    personalization?: {
      note?: string;
      history_used?: number;
    };
    fallback?: {
      type: 'unknown_intent' | 'rag';
      reason?: string;
    };
  };
}

export interface User {
  id: number;
  external_id?: string;
  name?: string;
  preferred_name?: string;
  email?: string;
  phone?: string;
  locale?: string;
  timezone?: string;
  marketing_opt_in: number;
  city?: string;
  state?: string;
  country?: string;
  avatar_url?: string;
  last_intent?: string;
  last_seen_at?: string;
  preferences?: string;
  notes?: string;
  created_at: string;
  updated_at: string;
}
