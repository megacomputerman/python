#######################################################################
# Nome do Arquivo: functions.py
# Autor: Wallace Duarte
# Descrição: Noções básicas de funcoes
######################################################################

# Usado para passar parametros via linha do terminal
import sys

#
# Funcao para somar 2 numeros
#
def soma(a, b):
    if a is None or b is None:
        print("Paremtro invalido")
        return None
    
    return a + b

# Pega os parametros passados no terminal, se nao for passado os 2 params 
# no terminal ocorre erro.
# exemplo de chamada no windows:  py functions.py 5 5
a = int(sys.argv[1])
b = int(sys.argv[2])

# Faz a soma e imprime o resultado
ret = soma(a, b)
print(a, "+", b, " = ", ret); 


#
# Funcao para verificar se o numero eh par
#
def numero_par(numero):
    if numero is None:
        print("Parametro invalido")
        return None
    
    if numero % 2 == 0:
        return True
    else:
        return False;

numero = int(sys.argv[1])
if numero_par(numero):
    print(numero, " eh par")
else:
    print(numero, " eh impar")
    

#
# Funcao para calcular o fatorial
#   
def fatorial(numero):
    if numero is None:
        print("Param invalido")
        return None
    
    fat = 1
    for i in range(1, numero + 1):
        fat *= i;
    return fat
    
ret = fatorial(numero)
print(numero,"!"," = ",ret);


