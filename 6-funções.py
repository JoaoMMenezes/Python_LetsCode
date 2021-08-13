'''
------------------------- FUNÇÕES -----------------------------
Sintaxe:
def nome_da_função(parâmetros):
    instruções
'''
def ola(nome, sobrenome):
    print("Olá, ", nome, sobrenome)
ola(input("Seu nome:"), input("Seu sobrenome:"))

# Os parâmetros passados podem ser especificados quando a função é 
# chamada, para isso só precisa fazer por ex: ola(sobrenome=Reis, nome=João)

# ------------------ FUNÇÕES COM RESPOSTA -------------------
# Usa "return" dentro da definição da função para retornar um valor

def somatorio(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

numeros = [1, 2, 3, 4, 5]
soma_dos_numeros = somatorio(numeros)
print("A soma dos elementos da lista vale: ", soma_dos_numeros)

if somatorio(numeros) > 50:
    print("Que soma grande!")
else:
    print("Que soma pequena!")
    
'''
Saída:
A soma dos elementos da lista vale:  15
Que soma pequena!
'''

# ---------------- FUNÇÕES RECURSIVAS ------------------
# Chamam outras funções
def funcaoRecursiva(numero):
    if (numero != 1):
        funcaoRecursiva(numero - 1)
    print(numero)

print("Testando a função recursiva:")
funcaoRecursiva(10)

# ---------------- PASSANDO INFINITOS PARÂMETROS ------------------
# Para fazer isso precisamos usar o (*args), o nome args é apenas uma convenção.
# é do tipo tupla.
def calculaMedia(*args):
    soma = sum(args)
    media = soma / len(args)
    return media

# Caso tenha que passar algum parâmetro que não são os args é preciso
# especificar eles na chamada da função. Ex: 
def calculaMedia(*args, nome):
    soma = sum(args)
    media = soma / len(args)
    return (f"{nome}, sua média é: {media}")
print(calculaMedia( 5, 8, 9, 14, nome="João"))

# Existe um jeito de passar parâmetros do typo dicionário, para usá-los só é 
# preciso usar (**kworks). Durante a chamada da função os parâmetros passados 
# precisam ser nomeados. Ex:
def piscina(prof, **infos):
    vol = prof*infos['largura']*infos['comprimento']
    return vol

volume = piscina(5, largura=4, comprimento=5)

print('O volume é: ', volume)

# Dá pra usar isso para PASSAR um dicionário para o parâmetro de uma função:
def piscina(prof, largura=4, comprimento=5):
    vol = prof*largura*comprimento
    return vol

infos = {'largura': 10, 'comprimento': 20}

volume = piscina(5, **infos)

print('O volume é: ', volume)