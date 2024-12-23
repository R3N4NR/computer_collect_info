from services.disks.UpdateDisks import update_disks
from services.disks.ListDisks import list_disks
from services.disks.CreateDisks import create_disks
import logging
from datetime import datetime

def manage_disks(id_computador, partitions):
    # Obter discos existentes
    existing_disks = list_disks(id_computador) or []
    
    # Extrair unidades já registradas
    existing_units = {disk['unidade'] for disk in existing_disks if 'unidade' in disk}
    logging.debug(f"Unidades existentes para o computador {id_computador}: {existing_units}")
    print(existing_disks)
    
    # Processar cada partição
    for disk in partitions:
        send_disk_data = {
            'id_computador': id_computador,
            'unidade': disk['unidade'],
            'disco_total': disk['espaco_total_GB'],
            'disco_livre': disk['espaco_livre_GB'],
            'disk_percent': disk['uso_percentual'],
            'data_coleta': datetime.now().isoformat()
            
        }
        
        if disk['unidade'] not in existing_units:
            logging.info(f"Registrando dados do disco {disk['unidade']}")
            create_disks(send_disk_data)
        else:
            logging.info(f"Disco {disk['unidade']} já registrado.")
            logging.info(f"Atualizando disco {disk['unidade']}...")
            update_disks(id_computador, send_disk_data)  # Passando send_disk_data aqui
