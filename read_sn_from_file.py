#######################################################################
# Nome do Arquivo: read_sn_from_file.py
# Autor: Wallace Duarte
# Descrição: Utilidades no uso de arquivos - ler sn do arquvio e comparar
######################################################################

# Usado para passar parametros via linha do terminal
import sys

# Usado para listar o diretorio
import os 

def exist_sn_number(serial, nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            if serial in conteudo:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return False

# Exemplo de uso
device_sn = "ABCDE12345"
nome_do_arquivo_txt = "SN.txt"

if exist_sn_number(device_sn, nome_do_arquivo_txt):
    print("O serial existe no arquivo.")
else:
    print("O serial não existe no arquivo.")
