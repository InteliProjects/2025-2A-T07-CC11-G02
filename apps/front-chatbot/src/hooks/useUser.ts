import { useState, useCallback } from 'react';
import { userApi } from '@/services/api';
import type { User } from '@/types/chat';

export const useUser = () => {
  const [currentUser, setCurrentUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Buscar usuário por external_id
  const getUserByExternalId = useCallback(async (externalId: string) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const user = await userApi.getUserByExternalId(externalId);
      setCurrentUser(user);
      return user;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Erro ao buscar usuário';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  // Criar usuário
  const createUser = useCallback(async (userData: Partial<User>) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const user = await userApi.createUser(userData);
      setCurrentUser(user);
      return user;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Erro ao criar usuário';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  // Atualizar usuário
  const updateUser = useCallback(async (userId: number, userData: Partial<User>) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const user = await userApi.updateUser(userId, userData);
      setCurrentUser(user);
      return user;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Erro ao atualizar usuário';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  // Limpar usuário atual
  const clearUser = useCallback(() => {
    setCurrentUser(null);
    setError(null);
  }, []);

  return {
    currentUser,
    isLoading,
    error,
    getUserByExternalId,
    createUser,
    updateUser,
    clearUser,
  };
};
