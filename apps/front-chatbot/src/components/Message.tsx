import React from 'react';
import { User, Heart } from 'lucide-react';
import type { Message as MessageType } from '@/types/chat';

interface MessageProps {
  message: MessageType;
}

const Message: React.FC<MessageProps> = ({ message }) => {
  const formatTime = (date: Date) => {
    return date.toLocaleTimeString('pt-BR', {
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  return (
    <div className={`flex items-start space-x-4 animate-fade-in ${
      message.isUser ? 'flex-row-reverse' : ''
    }`}>
      {/* Avatar */}
      <div className="flex-shrink-0">
        {message.isUser ? (
          <div className="w-10 h-10 rounded-2xl bg-gradient-to-br from-primary-500 to-primary-600 flex items-center justify-center shadow-lg">
            <User size={16} className="text-white" />
          </div>
        ) : (
          <div className="relative">
            <div className="flex-shrink-0 w-10 h-10 rounded-2xl bg-white/90 backdrop-blur-sm text-primary-700 border border-white/30 shadow-glass flex items-center justify-center">
              <span className="text-lg font-bold text-primary-500">C</span>
            </div>
            <div className="absolute -bottom-1 -right-1 w-4 h-4 bg-primary-500 rounded-full border-2 border-white animate-pulse"></div>
          </div>
        )}
      </div>

      {/* Message Content */}
      <div className={`flex flex-col max-w-[80%] ${message.isUser ? 'items-end' : 'items-start'}`}>
        <div
          className={`message-bubble ${
            message.isUser
              ? 'message-user animate-slide-in-right'
              : 'message-bot animate-slide-in-left'
          }`}
        >
          <p className="text-sm leading-relaxed whitespace-pre-wrap font-medium">
            {message.text}
          </p>
          
          {/* Decorative element for bot messages */}
          {!message.isUser && (
            <div className="absolute -top-1 -right-1 w-3 h-3 bg-primary-500/20 rounded-full"></div>
          )}
        </div>

        {/* Timestamp */}
        <div className={`flex items-center space-x-1 mt-2 ${message.isUser ? 'flex-row-reverse' : ''}`}>
          <span className="text-xs text-neutral-400 font-light">
            {formatTime(message.timestamp)}
          </span>
          {!message.isUser && (
            <Heart size={12} className="text-primary-500 animate-pulse" />
          )}
        </div>
      </div>
    </div>
  );
};

export default Message;