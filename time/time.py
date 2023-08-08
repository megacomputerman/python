#######################################################################
# Nome do Arquivo: time.py
# Autor: Wallace Duarte
# Descrição: Noções básicas de funcoes de tempo 
######################################################################

# funcoes de tempo
from datetime import datetime, timedelta
import time
import schedule


#Verifica se eh dia da semana1:
def dia_util():
    agora = datetime.now()
    return agora.weekday() < 5 # retorna true

#Verifica se eh dia da semana2:
def semana():
    # 0 a 6 | de segunda a domingo:
    data_atual = datetime.now()
    dia_semana = data_atual.weekday()

    # de segunda a sexta
    semana = (0, 1, 2, 3, 4)

    if dia_semana in semana:
        return True
    else:
        return False

if semana():
    print("eh dia da semana")
    
#soma dos tempos no formato %H:%M
def minha_soma_tempo():
    formato = "%H:%M"
    hora1_obj = datetime.now()
    hora2_obj = timedelta(hours=9, minutes=48)
    soma = hora1_obj + hora2_obj
    resultado = soma.strftime(formato)
    return resultado
    

formato = "%H:%M"
hora_atual = datetime.now().strftime(formato)
print(hora_atual)
hora_soma = minha_soma_tempo()
print(hora_soma)
  
# Dispara uma evento todos os dias da semana as 08:09
def evento():
    print("Evento disparado!")

schedule.every().day.at("08:09").do(evento)

while True:
    if dia_util:
        schedule.run_pending()
    time.sleep(40)
