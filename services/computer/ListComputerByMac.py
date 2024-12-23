import os
import requests
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Obter a URL da API do .env
API_URL = os.getenv("API_URL")

def buscar_computadores_por_mac(mac_address):
    try:
        # Montar a URL completa da rota
        url = f"{API_URL}/list-computer"

        # Fazer a requisição GET
        response = requests.get(url, params={"mac": mac_address})

        # Verificar o status da resposta
        if response.status_code == 200:
            # Retornar os dados em JSON
            return response.json()
        else:
            print(f"Erro: {response.status_code} - {response.json().get('detail')}")
            return None

    except Exception as e:
        print(f"Erro ao conectar com a API: {str(e)}")
        return None

