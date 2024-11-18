import os

# Config.py
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError("A chave da API não foi definida como variável de ambiente.")