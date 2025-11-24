import React, { useState } from 'react';
import ChatInterface from './components/ChatInterface';
import UserProfile from './components/UserProfile';
import { User as UserIcon, MessageCircle } from 'lucide-react';
import type { User } from './types/chat';

function App() {
  const [, setCurrentUser] = useState<User | null>(null);
  const [showUserProfile, setShowUserProfile] = useState(false);
  
  // Gerar um external_id único para o usuário (em produção, isso viria de autenticação)
  const externalId = React.useMemo(() => {
    const stored = localStorage.getItem('curadobia_external_id');
    if (stored) return stored;
    
    const newId = `web_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    localStorage.setItem('curadobia_external_id', newId);
    return newId;
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 via-white to-secondary-50 relative overflow-hidden">
      {/* Background decorative elements */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-20 left-10 w-72 h-72 bg-fashion-gold/5 rounded-full blur-3xl animate-float"></div>
        <div className="absolute bottom-20 right-10 w-96 h-96 bg-primary-500/5 rounded-full blur-3xl animate-float" style={{ animationDelay: '2s' }}></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-secondary-500/5 rounded-full blur-3xl animate-float" style={{ animationDelay: '4s' }}></div>
      </div>
      
      {/* Main content */}
      <div className="relative z-10">
        {/* Navigation */}
        <div className="fixed top-4 right-4 z-20 flex items-center space-x-2">
          <button
            onClick={() => setShowUserProfile(!showUserProfile)}
            className="p-3 bg-white/80 backdrop-blur-sm rounded-xl border border-white/40 shadow-fashion hover:shadow-fashion-lg transition-all duration-300 hover:scale-105"
            title={showUserProfile ? 'Fechar perfil' : 'Ver perfil'}
          >
            {showUserProfile ? <MessageCircle size={18} className="text-primary-600" /> : <UserIcon size={18} className="text-primary-600" />}
          </button>
        </div>

        {/* User Profile Sidebar */}
        {showUserProfile && (
          <div className="fixed top-4 right-4 z-30 w-80 max-h-[calc(100vh-2rem)] overflow-y-auto">
            <UserProfile 
              externalId={externalId} 
              onUserChange={setCurrentUser}
            />
          </div>
        )}

        {/* Chat Interface */}
        <ChatInterface externalId={externalId} />
      </div>
    </div>
  );
}

export default App;
