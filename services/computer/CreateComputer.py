import os
import requests
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Obter a URL da API do .env
API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("A variável de ambiente API_URL não está definida ou não foi carregada.")

def criar_computador(hostname, mac):
    try:
        # Montar a URL completa da rota
        url = f"{API_URL}/create-computer"
        
        # Dados do computador
        payload = {
            "hostname": hostname,
            "mac": mac
        }
        
        # Fazer a requisição POST com timeout
        response = requests.post(url, json=payload, timeout=10)
        
        # Verificar o status da resposta
        if response.status_code == 200:
            # Retornar os dados em JSON
            return response.json()
        else:
            print(f"Erro: {response.status_code} - {response.json().get('detail')}")
            return None

    except requests.exceptions.Timeout:
        print("Erro: A requisição excedeu o tempo limite.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {str(e)}")
        return None

