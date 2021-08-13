# ------------------------------- LISTAS --------------------------------
# Criando uma lista vazia.
listavazia = []

# Criando uma lista com alguns valores.
numeros = [1, 3, 7, 8, 9]

# Listas podem mesclar diferentes tipos de valores.
listamista = [14, "let's code", 0.1, True]

# Acessamos cada elemento da lista através de um índice entre colchetes.
# Os índices começam em 0.
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])

# Listas são mutáveis: podemos alterar o valor de seus itens.
numeros[2] = 5
print(numeros)

# Um jeito inteligente de trabalhar com listas é utilizando loops.
indice = 0
while indice < 5:
    print(numeros[indice])
    indice = indice + 1

# Pode-se usar a função "len()" de lenght para obter o tamanho da lista
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice = indice + 1

# ------------------- SLICING Modos de acessar indexs das listas -------------------
paises = ["Brasil", "Alemanha", "Russia", "Itália", "Japão"]
print(paises)
    # OBS: O ÍNDICE FINAL N É INCLUÍDO
print("[1:3] =", paises[1:3])
print("[1:-1] =", paises[1:(-1)])
print("[2:] =", paises[2:])
print("[:3] =", paises[:3])
print("[:] =", paises[:])
print("[::2] =", paises[::2])
print("[::-1] =", paises[::-1])

#  -------------------- Métodos para usar com listas -----------------------
# Para INCREMENTAR uma lista, AUMENTANDO seu TAMANHO, usamos a função .append()
listaDeCompras = ["ovo", "leite", "trigo"]
listaDeCompras.append(input("O que deseja colocar na lista de compras?"))
print("Lista atual:", listaDeCompras)

res = input("Deseja deletar um item? (S ou N)")
while (res == "S"):
    retirar = input("O que quer retirar da lista?")

    # .remove() retira um item da lista(Acusa erro se não houver o exato item na lista)
    listaDeCompras.remove(retirar)                  

    print("Lista atual:", listaDeCompras)
    res = input("Deseja deletar um item? (S ou N)")

print("Lista atual:", listaDeCompras)
print("Alterações finalizadas!")


# .count() conta quantas vezes um elemento aparece.
listaGenerica = [0, 1, 8, 14, 2, 3, 3, 4, 5, 5, 5, 6]
listaDeCompras = ["ovo", "leite", "trigo"]
print("Usando .count():", listaGenerica.count(5))

# .index() busca em um elemento e fala em qual a primeira posição que ele aparece.
print("Usando .index():", listaGenerica.index(5))

# .sort() ordena uma lista. (não pode ser passada dentro do print)
listaGenerica.sort()                        
print("Usando .sort():", listaGenerica)
listaGenerica.sort(reverse=True)
print("Usando .sort():", listaGenerica)

#.insert(index, item) coloca um item na lista no index especificado.
itens = ['a', 'b', 'c', 'E']
itens.insert(3, "d")
print(itens)

# As funções max(lista) e min(lista) obtém, respectivamente, o maior e o menor valor.
digitos = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maior = max(digitos)
menor = min(digitos)
print(digitos)
print("Maior = ", maior, "e menor = ", menor)


def f_it(n):
    resultado = 1

    for i in range(1, n+1, 1):
        resultado = resultado * i
  
    return resultado
print(f_it(3))


def f_rec(n):
    if n != 0:
        return n*f_rec(n-1)
    return 1
print(f_rec(3))