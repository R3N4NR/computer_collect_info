import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Obter a URL da API do .env
API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("A variável de ambiente API_URL não está definida ou não foi carregada.")
def list_metrics(id_computador):
    """
    Obtém os dados de monitoramento de um computador específico pelo endpoint '/list-monitoramento'.
    
    :param id_computador: UUID do computador.
    :return: Resposta da API.
    """
    try:
        url = f"{API_URL}/list-monitoramento"
        params = {"id": str(id_computador)}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro: {response.status_code} - {response.json().get('detail')}")
            return None

    except Exception as e:
        print(f"Erro ao conectar com a API: {str(e)}")
        return None