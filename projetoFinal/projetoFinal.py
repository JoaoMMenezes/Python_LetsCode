import requests as r
import datetime as dt
import csv

from requests.api import options

url = 'https://api.covid19api.com/dayone/country/brazil'
res = r.get(url)

rawData = res.json()

finalData = []
for obs in rawData:
    finalData.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(finalData)):
    finalData[i][DATA] = finalData[i][DATA][:10]

with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(finalData)

for i in range(1, len(finalData)):
    finalData[i][DATA] = dt.datetime.strptime(finalData[i][DATA], '%Y-%m-%d') 


def getDatasets(y, labels):
    # Considera 2 casos diferentes. Passando uma lista ou apenas um item
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [{
            'label': labels[0],
            'data': y 
        }]

def setTitle(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }

def createChart( x, y, labels, kind='bar', title=''):
    datasets = getDatasets(y, labels)
    options = setTitle(title)

    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart

def getApiChart(chart):
    baseURL = 'https://quickcharts.io/chart'
    res = r.get(f"{baseURL}?c={str(chart)}")
    return res.content

def saveImage(path, content):
    with open(path, 'wb') as image:     # Usa-se 'wb' pois está sendo escrito em binário
        image.write(content)

# Para mostrar o gráfico no Jupyter Notebook:
from PIL import Image
from IPython.display import display 

def displayImage(path):
    imgPil = Image.open(path)
    display(imgPil)

# Criando o gráfico:
yData1 = []
for obs in finalData[1::10]:  # Pulando de 10 em 10 desconsiderando o header
    yData1.append([obs[CONFIRMADOS]])

yData2 = []
for obs in finalData[1::10]:  # Pulando de 10 em 10 desconsiderando o header
    yData1.append([obs[RECUPERADOS]])

x =[]
for obs in finalData[1::10]:
    x.append(obs[DATA].strftime('%d/%m%Y'))

chart = createChart(x, [yData1, yData2], labels, title='Gráfico Confirmados vs Recuperados')
chartContent = getApiChart(chart)
saveImage('meu-primeiro-gráfico.png', chartContent)
displayImage('meu-primeiro-gráfico.png')

# ------ GERENDO UM QRCODE PARA O GRÁFICO -------------
def getApiQrcode(link):
    text = quote(link)
    urlBase = 'https://quickchart.io/qr'
    res = r.get(f"{urlBase}?text={text}")
    return res.content

baseURL = 'https://quickcharts.io/chart'
link = f"{baseURL}?c={str(chart)}"
saveImage('qrcode.png', getApiQrcode(link))
displayImage('qrcode.png')

x = (False and False)
print(x)