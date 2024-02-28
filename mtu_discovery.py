import os

def test_mtu(destination, packet_size):
    try:
        # Executa o ping com o tamanho do pacote especificado
        response = os.system(f"ping {destination} -l {packet_size} -f")
        if response == 0:
            print(f"MTU de {packet_size} bytes é suportado até {destination}.")
        else:
            print(f"MTU de {packet_size} bytes não é suportado até {destination}.")
    except Exception as e:
        print(f"Erro ao executar o teste: {e}")

# Exemplo de uso
destination_ip = "8.8.8.8"  # Substitua pelo destino desejado
packet_size = 1461  # Tamanho do pacote em bytes

test_mtu(destination_ip, packet_size)
