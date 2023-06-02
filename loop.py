#######################################################################
# Nome do Arquivo: loop.py
# Autor: Wallace Duarte
# Descrição: Noções básicas das estrutura de controle de fluxo
######################################################################

# Estrutura de controle de fluxo: condicional e loop
# Basicamente temos o if, elif e else como condição e while and for como loop 
# break, continue, try, except and finally

# Exemplo de if, elif, else:
idade=18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

idade=17
if idade < 18:
    print("Menor de idade")
elif idade < 30:
    print("Jovem")
else:
    print("Adulto")

# Exemplo de while
print("Exemplo de while:")
index = 0
while index < 10:
    print(index)
    index += 1
    
print("Exemplo de for:")
for i in range(10):
    print(i)

# Exemplo do break, serve para interromper o loop
print("Exemplo de break:")
for i in range(11):
    if i == 3:
        break
print(i)

# O continue pula uma instrução do loop
# no exemplo abaixo o continue é usado para pular quando o numero for impar, 
# imprimindo apenas os numeros pares
print("Exemplo de continue:")
for i in range(11):
    if i % 2 != 0:
        continue
    print(i)

nomes = [ "joão", "aline", "jack", "me", "julina" ]
for nome in nomes:
    if nome == "jack":
        continue
    print(nome)
