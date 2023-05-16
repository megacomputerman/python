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

###########################################################
#Exemplo de lista
###########################################################
print("Exemplo de lista:")

# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

# Imprimindo a lista
print(numeros)  # Output: [1, 2, 3, 4, 5]

# Acessando elementos da lista pelo índice
primeiro_elemento = numeros[0]
segundo_elemento = numeros[1]
print(primeiro_elemento)  # Output: 1
print(segundo_elemento)  # Output: 2

# Modificando um elemento da lista
numeros[2] = 10
print(numeros)  # Output: [1, 2, 10, 4, 5]

# Adicionando um elemento no final da lista
numeros.append(6)
print(numeros)  # Output: [1, 2, 10, 4, 5, 6]

# Removendo um elemento da lista
numeros.remove(2)
print(numeros)  # Output: [1, 10, 4, 5, 6]

# Obtendo o tamanho da lista
tamanho = len(numeros)
print(tamanho)  # Output: 5

# Imprimindo os elementos da lista
for numero in numeros:
    print(numero)
    

###########################################################
#Exemplo de tupla
###########################################################
print("Exemplo de tupla:")

# Criando uma tupla de coordenadas
coordenadas = (10, 20)

# Imprimindo a tupla
print(coordenadas)  # Output: (10, 20)

# Acessando elementos da tupla pelo índice
x = coordenadas[0]
y = coordenadas[1]
print(x)  # Output: 10
print(y)  # Output: 20

# Desempacotando uma tupla
x, y = coordenadas
print(x)  # Output: 10
print(y)  # Output: 20

# Tentando modificar um elemento da tupla (gerará um erro)
# coordenadas[0] = 5

# imprimindo os elementos da tupla
for valor in coordenadas:
    print(valor)
    
###########################################################
#Exemplo de conjunto
###########################################################
print("Exemplo de conjunto:")

# Criando um conjunto de números primos
numeros_primos = {2, 3, 5, 7}

# Imprimindo o conjunto
print(numeros_primos)  # Output: {2, 3, 5, 7}

# Verificando se um número está presente no conjunto
print(2 in numeros_primos)  # Output: True
print(4 in numeros_primos)  # Output: False

# Adicionando um elemento ao conjunto
numeros_primos.add(11)
print(numeros_primos)  # Output: {2, 3, 5, 7, 11}

# Removendo um elemento do conjunto
numeros_primos.remove(3)
print(numeros_primos)  # Output: {2, 5, 7, 11}

# Realizando operações de conjuntos
outros_numeros = {4, 6, 8, 10}
uniao = numeros_primos.union(outros_numeros)
intersecao = numeros_primos.intersection(outros_numeros)
diferenca = numeros_primos.difference(outros_numeros)

print(uniao)  # Output: {2, 4, 5, 6, 7, 8, 10, 11}
print(intersecao)  # Output: set()
print(diferenca)  # Output: {2, 5, 7, 11}

# Verificando se um conjunto é subconjunto de outro
print(numeros_primos.issubset(uniao))  # Output: True
print(outros_numeros.issubset(numeros_primos))  # Output: False

###########################################################
#Exemplo de dicionário
###########################################################
print("Exemplo de dicionário:")

# Criando um dicionário de informações de uma pessoa
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Imprimindo o dicionário
print(pessoa)  # Output: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Acessando valores no dicionário
nome = pessoa["nome"]
idade = pessoa["idade"]
print(nome)  # Output: João
print(idade)  # Output: 30

# Modificando valores no dicionário
pessoa["idade"] = 35
print(pessoa)  # Output: {'nome': 'João', 'idade': 35, 'cidade': 'São Paulo'}

# Adicionando um novo par de chave-valor no dicionário
pessoa["profissao"] = "Engenheiro"
print(pessoa)  # Output: {'nome': 'João', 'idade': 35, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}

# Removendo uma chave do dicionário
del pessoa["cidade"]
print(pessoa)  # Output: {'nome': 'João', 'idade': 35, 'profissao': 'Engenheiro'}

# Obtendo todas as chaves do dicionário
chaves = pessoa.keys()
print(chaves)  # Output: dict_keys(['nome', 'idade', 'profissao'])

# Obtendo todos os valores do dicionário
valores = pessoa.values()
print(valores)  # Output: dict_values(['João', 35, 'Engenheiro'])

# Iterando sobre as chaves e valores do dicionário
for chave, valor in pessoa.items():
    print(chave, ":", valor)