import os
import requests
from dotenv import load_dotenv
from utils.errors import api_url_error
import uuid

# Carrega as variáveis de ambiente
load_dotenv()

# Obter a URL da API do .env
API_URL = os.getenv("API_URL")

# Valida a URL da API
api_url_error(API_URL)

def update_metrics(id_computador: uuid.UUID, dados_monitoramento: dict):
    """
    Consome a rota '/update-metrics' para atualizar os dados de monitoramento.
    
    :param id_computador: ID do computador como objeto UUID.
    :param dados_monitoramento: Dados a serem atualizados em formato de dicionário.
    :return: Resposta da API ou mensagem de erro.
    """
    try:
        # Construir a URL completa
        url = f"{API_URL}/update-metrics"
        headers = {'Content-Type': 'application/json'}
        # Enviar a requisição PUT
        response = requests.put(
            url,
            params={"id_computador": str(id_computador)},  # Passar o UUID no parâmetro da URL
            json=dados_monitoramento,          # Dados do monitoramento no corpo da requisição
            timeout=10,
            headers=headers                         
        )
        
        # Verificar o status da resposta
        if response.status_code == 200:
            return response.json()  # Retorna os dados atualizados
        else:
            # Lidar com erros da API
            return {
                "status": response.status_code,
                "erro": response.json().get("detail", "Erro desconhecido")
            }
    except requests.exceptions.RequestException as e:
        return {"erro": f"Falha ao consumir a API: {str(e)}"}
