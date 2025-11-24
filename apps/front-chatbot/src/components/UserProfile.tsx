import React, { useState } from 'react';
import { User, Edit3, Save, X } from 'lucide-react';
import { useUser } from '@/hooks/useUser';
import type { User as UserType } from '@/types/chat';

interface UserProfileProps {
  externalId?: string;
  onUserChange?: (user: UserType | null) => void;
}

const UserProfile: React.FC<UserProfileProps> = ({ externalId, onUserChange }) => {
  const { currentUser, isLoading, error, createUser, updateUser, getUserByExternalId } = useUser();
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState<Partial<UserType>>({
    name: '',
    preferred_name: '',
    email: '',
    phone: '',
    city: '',
    state: '',
    country: '',
    marketing_opt_in: 0,
  });

  // Carregar usuário quando externalId mudar
  React.useEffect(() => {
    if (externalId && !currentUser) {
      getUserByExternalId(externalId).catch(() => {
        // Usuário não encontrado, será criado automaticamente
      });
    }
  }, [externalId, currentUser, getUserByExternalId]);

  // Notificar mudanças no usuário
  React.useEffect(() => {
    onUserChange?.(currentUser);
  }, [currentUser, onUserChange]);

  const handleEdit = () => {
    if (currentUser) {
      setFormData({
        name: currentUser.name || '',
        preferred_name: currentUser.preferred_name || '',
        email: currentUser.email || '',
        phone: currentUser.phone || '',
        city: currentUser.city || '',
        state: currentUser.state || '',
        country: currentUser.country || '',
        marketing_opt_in: currentUser.marketing_opt_in,
      });
    }
    setIsEditing(true);
  };

  const handleSave = async () => {
    try {
      if (currentUser) {
        await updateUser(currentUser.id, formData);
      } else if (externalId) {
        await createUser({
          external_id: externalId,
          ...formData,
        });
      }
      setIsEditing(false);
    } catch (err) {
      console.error('Erro ao salvar usuário:', err);
    }
  };

  const handleCancel = () => {
    setIsEditing(false);
    setFormData({
      name: '',
      preferred_name: '',
      email: '',
      phone: '',
      city: '',
      state: '',
      country: '',
      marketing_opt_in: 0,
    });
  };

  const handleInputChange = (field: keyof UserType, value: string | number) => {
    setFormData(prev => ({
      ...prev,
      [field]: value,
    }));
  };

  if (isLoading) {
    return (
      <div className="fashion-card p-4 rounded-xl">
        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 bg-primary-100 rounded-full animate-pulse"></div>
          <div className="flex-1">
            <div className="h-4 bg-primary-100 rounded animate-pulse mb-2"></div>
            <div className="h-3 bg-primary-100 rounded animate-pulse w-2/3"></div>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="fashion-card p-4 rounded-xl border-l-4 border-red-400">
        <div className="flex items-center space-x-2">
          <X size={16} className="text-red-500" />
          <span className="text-sm text-red-700 font-medium">
            Erro ao carregar perfil: {error}
          </span>
        </div>
      </div>
    );
  }

  return (
    <div className="fashion-card p-4 rounded-xl">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-600 rounded-full flex items-center justify-center text-white font-semibold">
            <User size={18} />
          </div>
          <div>
            <h3 className="font-semibold text-primary-900">
              {currentUser?.preferred_name || currentUser?.name || 'Usuário'}
            </h3>
            <p className="text-sm text-neutral-600">
              {currentUser ? 'Perfil ativo' : 'Novo usuário'}
            </p>
          </div>
        </div>
        
        <div className="flex items-center space-x-2">
          {!isEditing ? (
            <button
              onClick={handleEdit}
              className="p-2 text-primary-600 hover:bg-primary-50 rounded-lg transition-colors"
              title="Editar perfil"
            >
              <Edit3 size={16} />
            </button>
          ) : (
            <div className="flex items-center space-x-1">
              <button
                onClick={handleSave}
                className="p-2 text-green-600 hover:bg-green-50 rounded-lg transition-colors"
                title="Salvar"
              >
                <Save size={16} />
              </button>
              <button
                onClick={handleCancel}
                className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                title="Cancelar"
              >
                <X size={16} />
              </button>
            </div>
          )}
        </div>
      </div>

      {isEditing ? (
        <div className="space-y-3">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div>
              <label className="block text-sm font-medium text-neutral-700 mb-1">
                Nome
              </label>
              <input
                type="text"
                value={formData.name || ''}
                onChange={(e) => handleInputChange('name', e.target.value)}
                className="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500/30 focus:border-primary-300 text-sm"
                placeholder="Seu nome completo"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-neutral-700 mb-1">
                Nome preferido
              </label>
              <input
                type="text"
                value={formData.preferred_name || ''}
                onChange={(e) => handleInputChange('preferred_name', e.target.value)}
                className="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500/30 focus:border-primary-300 text-sm"
                placeholder="Como prefere ser chamada"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-neutral-700 mb-1">
                Email
              </label>
              <input
                type="email"
                value={formData.email || ''}
                onChange={(e) => handleInputChange('email', e.target.value)}
                className="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500/30 focus:border-primary-300 text-sm"
                placeholder="seu@email.com"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-neutral-700 mb-1">
                Telefone
              </label>
              <input
                type="tel"
                value={formData.phone || ''}
                onChange={(e) => handleInputChange('phone', e.target.value)}
                className="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500/30 focus:border-primary-300 text-sm"
                placeholder="(11) 99999-9999"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-neutral-700 mb-1">
                Cidade
              </label>
              <input
                type="text"
                value={formData.city || ''}
                onChange={(e) => handleInputChange('city', e.target.value)}
                className="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500/30 focus:border-primary-300 text-sm"
                placeholder="Sua cidade"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-neutral-700 mb-1">
                Estado
              </label>
              <input
                type="text"
                value={formData.state || ''}
                onChange={(e) => handleInputChange('state', e.target.value)}
                className="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500/30 focus:border-primary-300 text-sm"
                placeholder="Seu estado"
              />
            </div>
          </div>
          
          <div className="flex items-center space-x-2">
            <input
              type="checkbox"
              id="marketing"
              checked={formData.marketing_opt_in === 1}
              onChange={(e) => handleInputChange('marketing_opt_in', e.target.checked ? 1 : 0)}
              className="w-4 h-4 text-primary-600 border-neutral-300 rounded focus:ring-primary-500"
            />
            <label htmlFor="marketing" className="text-sm text-neutral-700">
              Aceito receber comunicações de marketing
            </label>
          </div>
        </div>
      ) : (
        <div className="space-y-2 text-sm text-neutral-600">
          {currentUser?.email && (
            <div className="flex items-center space-x-2">
              <span className="font-medium">Email:</span>
              <span>{currentUser.email}</span>
            </div>
          )}
          {currentUser?.phone && (
            <div className="flex items-center space-x-2">
              <span className="font-medium">Telefone:</span>
              <span>{currentUser.phone}</span>
            </div>
          )}
          {(currentUser?.city || currentUser?.state) && (
            <div className="flex items-center space-x-2">
              <span className="font-medium">Localização:</span>
              <span>
                {[currentUser.city, currentUser.state].filter(Boolean).join(', ')}
              </span>
            </div>
          )}
          {currentUser?.marketing_opt_in === 1 && (
            <div className="flex items-center space-x-2">
              <span className="text-green-600 text-xs">✓ Marketing opt-in</span>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default UserProfile;
