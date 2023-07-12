#######################################################################
# Nome do Arquivo: functions.py
# Autor: Wallace Duarte
# Descrição: Noções básicas de funcoes
######################################################################

# Usado para passar parametros via linha do terminal
import sys

# Usado para listar o diretorio
import os 

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

#
# Funcao para listar arquivos no diretorio usando lista
#  
def lista_arquivos(diretorio):
    arquivos = [] # liste arquivos
    for arquivo in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho):
            arquivos.append(arquivo)
    
    return arquivos

# Lista os arquivos do dir atual
diretorio = os.getcwd();
print(lista_arquivos(diretorio))


#
# Funcoes usando dicionario para adicionar e remover alunos
# 

estudantes = [
    {
        "nome": "Joao",
        "idade": 17,
        "serie": 3
    },
    {
        "nome": "wall",
        "idade": 18,
        "serie": 3
    }   
]

#
# imprime dicionarios aluno
# 
def imprime_alunos(estudantes):
    for estudante in estudantes:
        print(estudante)

imprime_alunos(estudantes)

#
# cria novo aluno
# 
def novo_aluno():
    nome = input("Nome: ")
    idade = input("Idade: ")
    serie = input("Serie: ")
    
    estudante = {
        "nome": nome,
        "idade": idade,
        "serie": serie
    }
    return estudante

#cria novo aluno, add na lista de estudantes e imprime a lista
novo_aluno = novo_aluno()
estudantes.append(novo_aluno)
imprime_alunos(estudantes)

#remover o estudante do indice 0 / primeiro aluno 
print("aluno removido: ")
aluno_removido = estudantes.pop(0)
print(aluno_removido)

def remove_pelo_nome(nome, estudantes):
    bRet = False
    for estudante in estudantes:
        if estudante["nome"] == nome:
            estudantes.remove(estudante)
            bRet = True
            break
    return bRet

aluno_removido_nome = remove_pelo_nome("wall", estudantes)
if aluno_removido_nome:
    print("aluno removido")
else:
    print("aluno nao removido ou nao encontrado")
