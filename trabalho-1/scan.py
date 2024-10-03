import socket

# Função para ler o arquivo /etc/services e mapear portas aos seus protocolos


def load_services():
    services = {}
    with open('/etc/services', 'r') as f:
        for row in f:
            slices = row.split()
            if len(slices) >= 2:
                service_name = slices[0]
                port_info = slices[1].split('/')
                if len(port_info) == 2:
                    port = int(port_info[0])
                    protocol = port_info[1]
                    services[port] = (service_name, protocol)
    return services

# Função principal para escanear as portas


def port_scan(ip, ports):
    services = load_services()
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)  # Tempo limite para a conexão
        code = client.connect_ex((ip, port))
        if code == 0:
            service = services.get(port, ("Desconhecido", "Desconhecido"))
            print(
                f"Porta {port} está ABERTA - Serviço: {service[0]}, Protocolo: {service[1]}")
        client.close()


# Definindo o IP e as portas a serem escaneadas
target_ip = '127.0.0.1'  # Endereço IP alvo (localhost)
ports = range(1, 65536)  # Intervalo de portas a serem escaneadas (1 a 65536)

# Iniciar o escaneamento
port_scan(target_ip, ports)
