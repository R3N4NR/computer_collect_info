import os
from dotenv import load_dotenv
import requests
from utils.errors import api_url_error

load_dotenv()

# Obter a URL da API do .env
API_URL = os.getenv("API_URL")

api_url_error(API_URL)


def create_disks( discos: dict):
    """
    Consome a rota '/create-disks' para enviar dados de discos ao servidor.
    :param discos: Dicionário com os dados dos discos para inserir.
    :return: Resposta da API ou mensagem de erro.
    """
    try:
        # Construir a URL completa
        url = f"{API_URL}/create-disks"

        # Enviar a requisição POST
        response = requests.post(url, json=discos)

        # Verificar o status da resposta
        if response.status_code == 201 or response.status_code == 200:
            return response.json()  # Retorna os dados em formato JSON
        else:
            # Lidar com erros de requisição
            return {
                "status": response.status_code,
                "erro": response.json().get("detail", "Erro desconhecido")
            }
    except Exception as e:
        return {"erro": f"Falha ao consumir a API: {str(e)}"}
