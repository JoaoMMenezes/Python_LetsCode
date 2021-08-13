'''
--------------------------------- CSV ------------------------------------------
O formato CSV (Comma Separated Values, ou Valores Separados por Vírgula)
é um arquivo de texto que representa dados em forma de tabela de forma simples.

Cada linha do arquivo de texto é uma linha da tabela, e as colunas são separadas por vírgulas.

Para se ler arquivos csv precisa importar uma biblioteca usando "import csv"
'''

import csv;
with open("zbrasilCovid.csv", "r", encoding="utf-8") as arquivoCSV:
    leitor = csv.reader(arquivoCSV) #pega o conteúdo do arquivo
    header = next(leitor)
    for linha in leitor:
        if float(linha[2] > 1):
            print(linha)

# Podemos ainda criar e escrever arquivos CSV:
import csv
with open("user.csv", "w", encoding="utf-8", newline="") as arquivoUser:
    escritor = csv.writer(arquivoUser) 
    escritor.writerow([ "nome", "sobrenome", "email", "genero"])
    escritor.writerow(['João', 'Menezes', 'joao@email.com', 'masculino'])

# -------------- Exemplo de CADASTRO usando a escrita de csv -----------
import csv
header = ['nome', 'sobrenome']
dados = []
opt = input("O que deseja fazer?\n1 - Cadastras\n0 - Sair")
while opt!= '0':
    nome = input("Seu nome:")
    sobrenome = input("Seu sobrenome:")
    dados.append([nome, sobrenome])     #Guarda os dados inseridos em uma lista de listas
    opt = input("O que deseja fazer?\n1 - Cadastras\n0 - Sair")

print(dados)

with open("userNames.csv", "w", encoding="utf-8", newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(header)
    writer.writerow(dados)

with open("userNames.csv", "r") as arquivoUsersNames:
    reader = csv.reader(arquivoUsersNames, delimiter=",")
    for row in reader:
        print(row)