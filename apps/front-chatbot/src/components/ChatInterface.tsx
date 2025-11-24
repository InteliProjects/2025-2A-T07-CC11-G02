import React from 'react';
import { useChat } from '@/hooks/useChat';
import ChatHeader from './ChatHeader';
import Message from './Message';
import ChatInput from './ChatInput';
import TypingIndicator from './TypingIndicator';
import { Sparkles, AlertCircle, WifiOff, RefreshCw } from 'lucide-react';

interface ChatInterfaceProps {
  externalId?: string;
  className?: string;
}

const ChatInterface: React.FC<ChatInterfaceProps> = ({
  externalId,
  className = '',
}) => {
  const { 
    messages, 
    isLoading, 
    error, 
    chatStatus, 
    sendMessage, 
    checkConnection, 
    messagesEndRef 
  } = useChat(externalId);

  const handleSendMessage = (message: string) => {
    if (!chatStatus.isOnline) {
      return;
    }
    sendMessage(message);
  };

  const handleRetryConnection = () => {
    checkConnection();
  };

  return (
    <div className={`chat-container ${className}`}>
      {/* Header */}
      <ChatHeader 
        isOnline={chatStatus.isOnline} 
        connectionStatus={chatStatus.connectionStatus}
        retryCount={chatStatus.retryCount}
        onToggleConnection={handleRetryConnection}
      />

      {/* Messages Area */}
      <div className="chat-messages">
        {/* Welcome message for empty chat */}
        {messages.length === 1 && (
          <div className="flex justify-center mb-8">
            <div className="fashion-card p-6 rounded-3xl max-w-md text-center animate-fade-in">
              <div className="flex items-center justify-center space-x-2 mb-3">
                <Sparkles size={20} className="text-fashion-gold" />
                <h3 className="text-lg font-display font-semibold gradient-text">
                  Bem-vinda à Curadobia
                </h3>
                <Sparkles size={20} className="text-fashion-gold" />
              </div>
              <p className="text-sm text-neutral-600 leading-relaxed">
                Sua curadoria de moda personalizada está pronta. Conte-me sobre seu estilo, ocasião ou dúvidas que tenho!
              </p>
            </div>
          </div>
        )}

        {messages.map((message) => (
          <Message key={message.id} message={message} />
        ))}
        
        {/* Typing Indicator */}
        {isLoading && (
          <TypingIndicator 
            stage={
              chatStatus.retryCount > 0 
                ? 'loading_model' 
                : 'thinking'
            } 
          />
        )}
        
        {/* Connection Status - Não mostrar durante carregamento */}
        {!chatStatus.isOnline && !isLoading && (
          <div className="flex justify-center animate-slide-up">
            <div className={`fashion-card p-4 rounded-2xl max-w-sm border-l-4 ${
              chatStatus.connectionStatus === 'disconnected' 
                ? 'border-orange-400' 
                : chatStatus.connectionStatus === 'error'
                ? 'border-red-400'
                : 'border-yellow-400'
            }`}>
              <div className="flex items-center space-x-2">
                {chatStatus.connectionStatus === 'disconnected' ? (
                  <WifiOff size={16} className="text-orange-500" />
                ) : chatStatus.connectionStatus === 'error' ? (
                  <AlertCircle size={16} className="text-red-500" />
                ) : (
                  <AlertCircle size={16} className="text-yellow-500" />
                )}
                <span className={`text-sm font-medium ${
                  chatStatus.connectionStatus === 'disconnected' 
                    ? 'text-orange-700' 
                    : chatStatus.connectionStatus === 'error'
                    ? 'text-red-700'
                    : 'text-yellow-700'
                }`}>
                  {chatStatus.lastError || 
                   (chatStatus.connectionStatus === 'disconnected' 
                     ? 'Sem conexão com o servidor' 
                     : chatStatus.connectionStatus === 'error'
                     ? 'Erro no servidor'
                     : 'Problema de conexão')}
                </span>
                <button
                  onClick={handleRetryConnection}
                  className={`ml-2 p-1 rounded-full transition-colors ${
                    chatStatus.connectionStatus === 'disconnected' 
                      ? 'hover:bg-orange-100' 
                      : chatStatus.connectionStatus === 'error'
                      ? 'hover:bg-red-100'
                      : 'hover:bg-yellow-100'
                  }`}
                  title="Tentar reconectar"
                >
                  <RefreshCw size={14} className={
                    chatStatus.connectionStatus === 'disconnected' 
                      ? 'text-orange-600' 
                      : chatStatus.connectionStatus === 'error'
                      ? 'text-red-600'
                      : 'text-yellow-600'
                  } />
                </button>
              </div>
              {chatStatus.retryCount > 0 && (
                <div className="mt-2 text-xs text-neutral-500">
                  Tentativas de reconexão: {chatStatus.retryCount}
                </div>
              )}
            </div>
          </div>
        )}
        
        {/* Error Message */}
        {error && (
          <div className="flex justify-center animate-slide-up">
            <div className="fashion-card p-4 rounded-2xl max-w-sm border-l-4 border-yellow-400">
              <div className="flex items-center space-x-2">
                <AlertCircle size={16} className="text-yellow-500" />
                <span className="text-sm text-yellow-700 font-medium">
                  {error}
                </span>
              </div>
            </div>
          </div>
        )}
        
        {/* Scroll anchor */}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <div className="chat-input-container">
        <ChatInput
          onSendMessage={handleSendMessage}
          isLoading={isLoading}
          disabled={!chatStatus.isOnline}
          placeholder={
            chatStatus.isOnline 
              ? 'Conte-me sobre seu estilo...' 
              : chatStatus.connectionStatus === 'disconnected'
              ? 'Sem conexão com o servidor...'
              : chatStatus.connectionStatus === 'error'
              ? 'Erro no servidor. Tente novamente...'
              : 'Problema de conexão...'
          }
        />
      </div>
    </div>
  );
};

export default ChatInterface;
