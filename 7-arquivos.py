# ------------------------- MANIPULAÇÃO DE ARQUIVOS -----------------------
# Podemos criar arquivos novos ou abrir arquivos já existentes utilizando a função open.
# Ela possui 2 argumentos: o caminho do arquivo e o modo de operação.

# MODOS       SÍMBOLOS        DESCRIÇÃO
#   read          r               lê um arquivos existente
#   write         w               cria um arquivo
#   append        a               abre um arquivo e adiciona informação ao FINAl dele
#   update        +               ao ser combinado com outros modos, permite alteração 
#                                 de arquivo já existente (ex: r+ abre um arquivo existente e permite modificá-lo)

'''
    Devemos sempre FECHAR um arquivo depois de usá-lo para que seja salvo e 
    que não deixe nenhuma falha de segurança. 
    Para fechar, usar nome_do_arquivo.close()
'''

arquivoCriado = open("criado.txt", "w")
arquivoCriado.write("linha 1\n")
arquivoCriado.write("linha 2")
arquivoCriado.close()   #necessário fechar para q seja salvo
print(arquivoCriado)

# ------------------- WITH -----------------------
# O comando with garante que o arquivo será fechado.
with open('teste.txt', 'r') as arquivolido:
   dados = arquivolido.read()
   print(dados)

# Lendo linha a linha do arquivo:
with open('teste.txt', 'r') as arquivolido:
   linha = arquivolido.readline()
   while linha != '':
       print(linha, end='')
       linha = arquivolido.readline()


# OU

with open('teste.txt', 'r') as arquivolido:
    for linha in arquivolido:
        print(linha, end='')