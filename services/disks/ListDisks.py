import os
from dotenv import load_dotenv
import requests
import uuid
from utils.errors import api_url_error

load_dotenv()

# Obter a URL da API do .env
API_URL = os.getenv("API_URL")

api_url_error(API_URL)

def list_disks(id_computador: str):
    """
    Consome a rota '/list-disks' para obter informações sobre os discos de um computador.
    :param id_computador: ID do computador como string (UUID).
    :return: Dados dos discos ou mensagem de erro.
    """
    if not API_URL:
        raise ValueError("A URL da API não está configurada no .env")

    try:
        url = f"{API_URL}/list-disks"
        response = requests.get(url, params={"id_computador": str(id_computador)}, timeout=10)

        if response.status_code == 200:
            disks = response.json()
            # Garantir que a resposta seja uma lista, mesmo que tenha apenas um disco
            return disks if isinstance(disks, list) else [disks]
        else:
            return {
                "status": response.status_code,
                "erro": response.json().get("detail", "Erro desconhecido")
            }
    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro na comunicação com a API: {str(e)}"}
