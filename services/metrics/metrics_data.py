from services.metrics.ListMetrics import list_metrics
from services.metrics.CreateMetrics import create_metrics
from services.metrics.UpdateMetrics import update_metrics
import logging

def manage_metrics(id_computador, metrics_data):
    exists_on_metrics = list_metrics(id_computador)
    if not exists_on_metrics:
        logging.info("Criando novo registro de métricas.")
        create_metrics(metrics_data)
    else:
        logging.info("Atualizando dados de métricas existentes.")
        update_metrics(id_computador, metrics_data)
