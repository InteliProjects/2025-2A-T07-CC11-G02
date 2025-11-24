import React, { useState, useRef, useEffect } from 'react';
import { Send, Paperclip, Heart } from 'lucide-react';

interface ChatInputProps {
  onSendMessage: (message: string) => void;
  isLoading: boolean;
  placeholder?: string;
  disabled?: boolean;
}

const ChatInput: React.FC<ChatInputProps> = ({
  onSendMessage,
  isLoading,
  placeholder = 'Conte-me sobre seu estilo...',
  disabled = false,
}) => {
  const [message, setMessage] = useState('');
  const [isFocused, setIsFocused] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  }, [message]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim() && !isLoading && !disabled) {
      onSendMessage(message);
      setMessage('');
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className="w-full max-w-lg mx-auto">
      {/* Main input container */}
      <div className="relative bg-white/80 backdrop-blur-sm rounded-xl border border-white/40 shadow-fashion p-2.5">
        <form onSubmit={handleSubmit} className="flex items-center space-x-2">
          {/* Attachment Button */}
          <button
            type="button"
            className="flex-shrink-0 p-1.5 text-primary-400 hover:text-primary-500 hover:bg-primary-50 rounded-lg transition-all duration-200 disabled:opacity-50"
            disabled={isLoading || disabled}
            title="Anexar inspiração (em breve)"
          >
            <Paperclip size={14} />
          </button>

          {/* Message Input Container */}
          <div className="flex-1 relative">
            <textarea
              ref={textareaRef}
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyPress={handleKeyPress}
              onFocus={() => setIsFocused(true)}
              onBlur={() => setIsFocused(false)}
              placeholder={placeholder}
              disabled={isLoading || disabled}
              className={`w-full px-3 py-2 bg-white/60 border border-primary-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500/30 focus:border-primary-300 resize-none min-h-[36px] max-h-24 text-primary-900 placeholder-primary-400 transition-all duration-200 text-sm ${
                disabled ? 'opacity-50 cursor-not-allowed' : ''
              }`}
              rows={1}
            />
            
            {/* Character count for longer messages */}
            {message.length > 100 && (
              <div className="absolute -bottom-4 right-0 text-xs text-primary-400">
                {message.length}/500
              </div>
            )}
          </div>

          {/* Send Button */}
          <button
            type="submit"
            disabled={!message.trim() || isLoading || disabled}
            className="flex-shrink-0 w-8 h-8 bg-gradient-to-r from-primary-500 to-primary-600 hover:from-primary-600 hover:to-primary-700 text-white rounded-lg transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed shadow-fashion hover:shadow-fashion-lg hover:scale-105 active:scale-95 flex items-center justify-center"
            title="Enviar mensagem"
          >
            {isLoading ? (
              <div className="w-3 h-3 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
            ) : (
              <Send size={14} className="transition-transform" />
            )}
          </button>
        </form>
      </div>
      
      {/* Quick suggestions */}
      {!message && (
        <div className={`flex items-center justify-center space-x-4 mt-3 text-xs transition-all duration-300 ${
          isFocused 
            ? 'text-primary-400 opacity-60' 
            : 'text-primary-600 opacity-100'
        }`}>
          <span className="flex items-center space-x-1.5 px-2.5 py-1 bg-white/40 rounded-full border border-white/60">
            <Heart size={10} className="text-primary-500" />
            <span className="font-medium">Dicas de estilo</span>
          </span>
          <span className="flex items-center space-x-1.5 px-2.5 py-1 bg-white/40 rounded-full border border-white/60">
            <span className="w-1.5 h-1.5 bg-primary-500 rounded-full"></span>
            <span className="font-medium">Curadoria personalizada</span>
          </span>
        </div>
      )}
    </div>
  );
};

export default ChatInput;
