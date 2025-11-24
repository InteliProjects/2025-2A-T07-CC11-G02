import React from 'react';
import { Wifi, WifiOff, AlertCircle, RefreshCw } from 'lucide-react';
import type { ConnectionStatus } from '@/types/chat';

interface ChatHeaderProps {
  isOnline?: boolean;
  connectionStatus?: ConnectionStatus;
  retryCount?: number;
  onToggleConnection?: () => void;
}

const ChatHeader: React.FC<ChatHeaderProps> = ({
  isOnline = true,
  connectionStatus = 'connected',
  retryCount = 0,
  onToggleConnection,
}) => {
  return (
    <div className="bg-primary-900">
      <div className="p-6 flex items-center justify-between">
        {/* Logo and Title */}
        <div className="flex items-center space-x-4">
          <div className="w-12 h-12 bg-white/10 rounded-2xl flex items-center justify-center border border-white/20">
            <span className="text-2xl font-bold text-white">C</span>
          </div>
          <div>
            <h1 className="text-2xl font-display font-semibold text-white tracking-wide">
              Curadobia
            </h1>
            <p className="text-sm text-white/80 font-light tracking-wider">
              Curadoria de Moda
            </p>
          </div>
        </div>

        {/* Connection Status */}
        <div className="flex items-center space-x-3">
          <button
            onClick={onToggleConnection}
            className={`flex items-center space-x-2 px-4 py-2 rounded-full transition-all duration-300 group border ${
              isOnline 
                ? 'bg-white/10 hover:bg-white/20 border-white/20' 
                : connectionStatus === 'error'
                ? 'bg-red-500/20 hover:bg-red-500/30 border-red-400/30'
                : 'bg-orange-500/20 hover:bg-orange-500/30 border-orange-400/30'
            }`}
            title={
              isOnline 
                ? 'Conectado' 
                : connectionStatus === 'error'
                ? 'Erro no servidor'
                : 'Desconectado'
            }
          >
            {isOnline ? (
              <Wifi size={16} className="text-green-400 group-hover:scale-110 transition-transform" />
            ) : connectionStatus === 'error' ? (
              <AlertCircle size={16} className="text-red-400 group-hover:scale-110 transition-transform" />
            ) : (
              <WifiOff size={16} className="text-orange-400 group-hover:scale-110 transition-transform" />
            )}
            <span className="text-sm font-medium text-white/90">
              {isOnline 
                ? 'Online' 
                : connectionStatus === 'error'
                ? 'Erro'
                : 'Offline'
              }
            </span>
            {retryCount > 0 && (
              <RefreshCw size={12} className="text-white/60 animate-spin" />
            )}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatHeader;
