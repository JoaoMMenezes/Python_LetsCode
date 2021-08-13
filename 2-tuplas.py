# Uma tupla é uma coleção de objetos que lembra muito as listas.

# Ao invés de colchetes, usamos parênteses para declarar as tuplas:
numeros = (1,2,3,5,7,11)

# Podemos declarar sem parênteses também:
numeros = 1,2,3,5,7,11

# Para acessar um valor, utilizamos a mesma sintaxe das listas:
print(numeros[4])
print(type(numeros))

'''
Porém, tuplas são imutáveis: não é possível adicionar ou modificar valores.
Descomentar a linha abaixo provocará erro de execução:
'''
# numeros[4] = 8

# Podemos gerar uma tupla a partir de uma lista...
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
tupla1 = tuple(lista1)
print(tupla1)

# ...ou uma lista a partir de uma tupla:
tupla2 = [1, 6, 1, 8]
lista2 = list(tupla2)
print(lista2)

# Também pode-se usar o unpacking com uma tupla:
a, b, c, d, e, f = numeros # "desempacota" a tupla numeros
print("O primeiro vale:", a, "e o ultimo vale:", f)