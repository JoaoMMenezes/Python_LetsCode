# A função print dispõe na tela as informações entre parênteses
print("Hello, wordl!")

# pode-se passar mais de uma informação separando por vírgulas:
x = 8
print("Tenho", x, "batatas")
# além disso aínda é possível fazer operações dentro do print:
print(2 + 3)

# ------------- VARIÁVEIS --------------
# Os tipos das variáveis são atribuídas automaticamente quando declaradas
a = 1
b = "ola"
c = 84.2
d = True
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# ------------- OPERAÇÕES ----------------
x = 50
y = 2
print(x + y)    # soma comum
print(x - y)    # subtração
print(x * y)    # multiplicação
print(x / y)    # divisão com saída float
print(x ** y)   # exponenciação
print(x // y)   # divisão inteira - ignora os valores dp da virgula
print(x % y)    # resto

# Existem operadores lógicos tbm
# "and" e "or"
# >, >=, <, <=, !=, ==

# ------------- INPUTS----------------
# Podemos ler valores do teclado com a função input().
# Ela permite que a gente passe uma mensagem para o usuário.
nome = input('Digite o seu nome: ')

# Tudo que é lido por input() é considerado uma string (str).
# Para tratar como outros tipos de dados é necessário realizar a conversão:
peso = float(input('Digite o seu peso: ')) # lê o peso como número real
idade = int(input('Digite a sua idade: ')) # lê a idade como número inteiro

print(nome, 'pesa', peso, 'kg e tem', idade, 'anos de idade.')

# ------------ CONDICIONAL ------------
# Podemos usar "if", "elif" e "else" para resolvermos problemas de condição
# Deve-se atentar para o fato de em Python n haver chaves de fechamento, mas sim ":".
# Por conta disso, o que está dentro ou fora da condicional é determinado pela identação.
numero = int(input("Digite um número:"))

if (numero < 10):
    print("Seu número é menor que 10!")
elif (numero >= 10 and numero < 20):
    print(numero, "está entre 10 e 20")
else:
    print(numero, "é maior que 20")

# -------------- REPETIÇÃO ------------
# Pode-se usar o while para fazer as repetições.
# Ele é executado enquando a expressão condicional dele for True
# Pode ser usado para fazer validações. Ex:
resposta = input('Digite OK: ')
while resposta != 'OK':
    resposta = input('Não foi isso que eu pedi, digite OK: ')

# O "Break" interrompe o último while