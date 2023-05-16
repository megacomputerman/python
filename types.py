###########################################################
# Nome do Arquivo: types.py
# Autor: Wallace Duarte
# Descrição: Noções básicas dos tipos em python
###########################################################

# Variáveis com python
# A linguagem é de alto nível, tipagem dinânica, você não precisa declarar tipos, 
# o interpretador faz isso para você.  


###########################################################
# Números inteiros
###########################################################
x = 10
y = -5
z = 0

###########################################################
# Números de ponto flutuante
###########################################################
pi = 3.14
valor = 2.5

###########################################################
# Booleanos
###########################################################
verdadeiro = True
falso = False

###########################################################
# Caracteres / Strings
###########################################################
nome = "João"
mensagem = 'Olá, mundo!'

###########################################################
# Listas
###########################################################
numeros = [1, 2, 3, 4, 5]
nomes = ["Maria", "João", "Carlos"]

###########################################################
# Tuplas (tuple), a diferença da tupla para lista é que
# na tupla os valores não podem ser alterados
###########################################################
coordenadas = (10, 20)
cores = ("vermelho", "azul", "verde")

###########################################################
# Conjuntos (set)
###########################################################
animais = {"cachorro", "gato", "pássaro"}
numeros_primos = {2, 3, 5, 7}

###########################################################
# Dicionários (dict)
###########################################################
pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}


###########################################################
# Conversões
###########################################################

#int -> float
###########################################################
x_float = float(x)
print(x_float)

#float -> int
###########################################################
x_int = int(x_float)
print(x_int)

#float -> string
###########################################################
my_string = str(x_float)
print(my_string)

#string -> boolean
###########################################################
my_string = "True"
x_boolean = bool(my_string)
print(x_boolean)

#operações matemáticas
###########################################################
a = 5
b = 3
#Adição
resultado = a + b
print(resultado)

#Subtração
resultado = a - b
print(resultado)

#Multiplicação
resultado = a * b
print(resultado)

#Divisão
resultado = a / b
print(resultado)

#Divisão com resultado inteiro
resultado = a // b
print(resultado)

#Resto da divisão (%):
resultado = a % b
print(resultado) 

#Potenciação (**):
resultado = a ** b
print(resultado)
