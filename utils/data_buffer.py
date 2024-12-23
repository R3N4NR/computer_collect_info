import logging
from queue import Queue


data_buffer = Queue()

def prepare_data_for_db(data):
    try:
        data_buffer.put(data)
        logging.info(f"Dados preparados e colocados no buffer: {data}")
    except Exception as e:
        logging.error(f"Erro ao preparar os dados para o buffer: {e}")