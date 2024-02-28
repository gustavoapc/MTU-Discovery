import os

def test_mtu(destination, max_packet_size):
    try:
        for packet_size in range(1000, max_packet_size + 1, 100):
            response = os.system(f"ping {destination} -l {packet_size} -f")
            if response == 0:
                print(f"MTU de {packet_size} bytes é suportado até {destination}.")
            else:
                print(f"MTU de {packet_size} bytes não é suportado até {destination}.")
    except Exception as e:
        print(f"Erro ao executar o teste: {e}")

destination_ip = input("Digite o endereço IP de destino: ")
max_packet_size= 1500
test_mtu(destination_ip,max_packet_size)
