import os
from dotenv import load_dotenv
import requests
from utils.errors import api_url_error

load_dotenv()

# Obter a URL da API do .env
API_URL = os.getenv("API_URL")

api_url_error(API_URL)

def create_metrics(dados_monitoramento):
    """
    Envia dados de monitoramento para a API no endpoint '/create-metrics'.
    
    :param dados_monitoramento: Dicionário contendo os dados do monitoramento.
    :return: Resposta da API.
    """
    try:
        url = f"{API_URL}/create-metrics"
        response = requests.post(url, json=dados_monitoramento)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro: {response.status_code} - {response.json().get('detail')}")
            return None

    except Exception as e:
        print(f"Erro ao conectar com a API: {str(e)}")
        return None

