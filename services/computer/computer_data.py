from services.computer.ListComputerByMac import buscar_computadores_por_mac
from services.computer.CreateComputer import criar_computador
import logging

def get_or_create_computer(mac, hostname):
    mac_exists = buscar_computadores_por_mac(mac)
    if not mac_exists:
        logging.info(f"Computador com MAC {mac} não existe. Criando novo registro.")
        criar_computador(hostname, mac)
        return None  # Indica que o computador foi criado
    return mac_exists[0]['id']
