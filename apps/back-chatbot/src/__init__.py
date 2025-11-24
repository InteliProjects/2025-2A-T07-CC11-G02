# Pacote src do chatbot Curadobia

# Importar configuração principal
from .core.config import CONFIG

# Importar aplicação principal
from .api.app import app

__all__ = ['CONFIG', 'app']