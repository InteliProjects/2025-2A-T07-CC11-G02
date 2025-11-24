import React from 'react';
import { Brain, Database } from 'lucide-react';

interface TypingIndicatorProps {
  stage?: 'thinking' | 'processing' | 'generating' | 'loading_model';
}

const TypingIndicator: React.FC<TypingIndicatorProps> = ({ stage = 'thinking' }) => {
  const getStageInfo = () => {
    switch (stage) {
      case 'processing':
        return {
          icon: <Database size={12} className="text-green-500" />,
          text: 'Processando dados...',
          color: 'text-green-400'
        };
      case 'generating':
        return {
          icon: <Brain size={12} className="text-blue-500" />,
          text: 'Gerando resposta...',
          color: 'text-blue-400'
        };
      case 'loading_model':
        return {
          icon: <Brain size={12} className="text-orange-500" />,
          text: 'Carregando modelo (primeira vez pode demorar até 10 minutos)...',
          color: 'text-orange-400'
        };
      default:
        return {
          icon: <Brain size={12} className="text-primary-500" />,
          text: 'Pensando...',
          color: 'text-primary-400'
        };
    }
  };

  const stageInfo = getStageInfo();
  return (
    <div className="flex items-start space-x-4 animate-fade-in">
      {/* Bot Avatar */}
      <div className="relative">
        <div className="flex-shrink-0 w-10 h-10 rounded-2xl bg-white/90 backdrop-blur-sm text-primary-700 border border-white/30 shadow-glass flex items-center justify-center">
          <span className="text-lg font-bold text-primary-500">C</span>
        </div>
        <div className="absolute -bottom-1 -right-1 w-4 h-4 bg-primary-500 rounded-full border-2 border-white animate-pulse"></div>
      </div>

      {/* Typing Animation */}
      <div className="flex flex-col items-start">
        <div className="message-bot message-bubble animate-scale-in">
          <div className="flex items-center space-x-2">
            <div className="flex space-x-1 ml-2">
              <div className="w-2 h-2 bg-primary-500 rounded-full animate-bounce" style={{ animationDelay: '0ms', animationDuration: '1.4s' }} />
              <div className="w-2 h-2 bg-primary-500 rounded-full animate-bounce" style={{ animationDelay: '200ms', animationDuration: '1.4s' }} />
              <div className="w-2 h-2 bg-primary-500 rounded-full animate-bounce" style={{ animationDelay: '400ms', animationDuration: '1.4s' }} />
            </div>
            <span className={`text-xs ${stageInfo.color} ml-2 flex items-center space-x-1`}>
              {stageInfo.icon}
              <span>{stageInfo.text}</span>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TypingIndicator;
