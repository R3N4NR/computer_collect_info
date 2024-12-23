from datetime import datetime
import logging
from services.computer.computer_data import get_or_create_computer
from services.disks.disks_data import manage_disks
from services.metrics.metrics_data import manage_metrics
from utils.collector import collect_data
from config.logging_config import setup_logging


def main():
    setup_logging()
    
    try:
        logging.info("Coletando métricas do sistema...")
        data = collect_data()
        logging.debug(f"Métricas coletadas: {data}")
        
        mac = data['mac']
        hostname = data['hostname']
        
        id_computador = get_or_create_computer(mac, hostname)
        if id_computador is None:
            return  # Finaliza caso o computador tenha sido criado
        
        metrics_data = {
            'id_computador': id_computador,
            'id_discos': None,
            'hostname': hostname,
            'ip_local': data['ip_local'],
            'cpu_info': data['cpu_info'],
            'cpu_percent': data['cpu_percent'],
            'memoria_total': data['memoria_total'],
            'memoria_livre': data['memoria_livre'],
            'ram_percent': data['ram_percent'],
            'data_coleta': datetime.now().isoformat()
        }
        
        manage_metrics(id_computador, metrics_data)
        manage_disks(id_computador, data['partitions'])
        
    except Exception as e:
        logging.critical(f"Erro fatal: {e}")
        raise

if __name__ == "__main__":
    main()
