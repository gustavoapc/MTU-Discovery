import socket
import struct
import os

def discover_mtu(dest_addr, packet_size=1500, timeout=20):
    try:
        # Criar um socket ICMP (protocolo raw)
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        
        # Definir o tempo limite para receber a resposta
        s.settimeout(timeout)
        
        # Configurar o endereço de destino e o tamanho do pacote
        dest = (dest_addr, 0)
        s.connect(dest)
        
        # Construir um pacote ICMP Echo Request com o bit "Don't Fragment" (DF) setado
        icmp_packet = b'\x08\x00\x00\x00\x00\x01\x00\x00'
        data = b'X' * (packet_size - len(icmp_packet))
        packet = icmp_packet + data
        
        # Enviar o pacote
        s.send(packet)
        
        # Receber a resposta
        reply = s.recv(4096)
        
        # Extrair o tamanho do pacote da resposta
        mtu = len(reply) + 28  # Tamanho do cabeçalho IP (20 bytes) + Tamanho do cabeçalho ICMP (8 bytes)
        
        return mtu
    
    except socket.error as e:
        print(f"Erro ao descobrir o MTU: {e}")
        return -1
    
    finally:
        s.close()

# Função principal
def main():
    dest_addr = input("Digite o endereço IP de destino: ")
    mtu = discover_mtu(dest_addr)
    
    if mtu == -1:
        print("Timeout ao tentar descobrir o MTU.")
    else:
        print(f"MTU para {dest_addr}: {mtu} bytes")

if __name__ == "__main__":
    main()
