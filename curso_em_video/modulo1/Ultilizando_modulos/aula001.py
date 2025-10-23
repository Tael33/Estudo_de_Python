import math  # Importa toda a Biblioteca de matematica
from math import sqrt # Impota apenas o elemento "sqrt", ou seja, importa só o elemanto selecionado apos a tag Importe
from math import sqrt, ceil # Impota apenas os elemento selecionado apos a tag Importe

# Elementos da biblioteca "math"

ceil # faz um aredondamento do numero pra cima
floor # faz um aredondamento do numero pra baixo
trunc # Elimina os numeros apos a virgula, sem aredondamento
pow # Potencia == **
sqrt # Raiz quadrado
factorial # fatorial " Multiplicação do número e dos números antecessores"
log # Logaritmo de um número em uma base especifica
log10 # Logaritmo de um número na base 10

# Exemplo de uso
num = int(input("Digite um número: "))
raiz = sqrt(num) # Raiz quadrada
print(f"A raiz de {num} é igual a {raiz:.2f}")
print(f"O fatorial de {num} é igual a {factorial(num)}")
print(f"O logaritmo de {num} na base 10 é igual a {log10(num):.2f}")
print(f"O logaritmo de {num} na base 2 é igual a {log(num, 2):.2f}")
print(f"O logaritmo de {num} na base e é igual a {log(num):.2f}")
valor = float(input("Digite um valor: "))
print(f"O valor arredondado para cima é {ceil(valor)}")
print(f"O valor arredondado para baixo é {floor(valor)}")   
print(f"O valor truncado é {trunc(valor)}")


import random # Importa toda a Biblioteca de randomicos
from random import random # Importa apenas o elemento "random", ou seja, importa só o elemanto selecionado apos a tag Importe
from random import random, randint # Importa apenas os elemento selecionado apos a tag Importe

# Elementos da biblioteca "random"
random # Gera um número aleatório entre 0 e 1
randint # Gera um número aleatório entre dois limites
uniform # Gera um número aleatório entre dois limites, com números quebrados
randrange # Gera um número aleatório dentro de um intervalo especifico
choice # Escolhe um elemento aleatório dentro de uma lista, tupla, dicionário, etc
shuffle # Embaralha os elementos de uma lista

# Exemplo de uso
num = random() # Gera um número aleatório entre 0 e 1
print(f"O número gerado foi {num:.2f}")

num = randint(1, 10) # Gera um número aleatório entre 1 e 10
print(f"O número gerado foi {num}")

num = uniform(1, 10) # Gera um número aleatório entre 1 e 10, com números quebrados
print(f"O número gerado foi {num:.2f}")

num = randrange(1, 10) # Gera um número aleatório dentro de um intervalo especifico
print(f"O número gerado foi {num}")
lista = ['Ana', 'Bruno', 'Camila', 'Daniel']
random.shuffle(lista) # Embaralha os elementos de uma lista
print(f"A lista embaralhada foi {lista}")


import emoji # Importa toda a Biblioteca de emojis
from emoji import emojize # Importa apenas o elemento "emojize", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "emoji"
emojize # Converte códigos de emojis em emojis
demojize # Converte emojis em códigos de emojis
    # Exemplo de uso    

print(emojize("Olá, Mundo! :earth_americas:", use_aliases=True))
print(emoji.emojize("Olá, Mundo! :earth_americas:", use_aliases=True))
print(emoji.demojize("Olá, Mundo! 🌎"))

import playsound # Importa toda a Biblioteca de sons
from playsound import playsound # Importa apenas o elemento "playsound", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "playsound"
playsound # Reproduz um arquivo de som  
    # Exemplo de uso
playsound('caminho/do/arquivo/de/som.mp3')

import pyttsx3 # Importa toda a Biblioteca de voz
from pyttsx3 import init # Importa apenas o elemento "init", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "pyttsx3"
init # Inicializa o conversor de texto em fala
say # Converte o texto em fala
runAndWait # Executa a fala
    # Exemplo de uso
engine = pyttsx3.init()
engine.say("Olá, Mundo!")
engine.runAndWait()

import webbrowser # Importa toda a Biblioteca de navegador web
from webbrowser import open # Importa apenas o elemento "open", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "webbrowser"
open # Abre uma URL em um navegador web
open_new # Abre uma URL em uma nova janela do navegador web
open_new_tab # Abre uma URL em uma nova aba do navegador web
    # Exemplo de uso
webbrowser.open('https://www.google.com')   
webbrowser.open_new('https://www.google.com')   
webbrowser.open_new_tab('https://www.google.com')

import time # Importa toda a Biblioteca de tempo
from time import sleep # Importa apenas o elemento "sleep", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "time"
sleep # Pausa a execução por um determinado tempo
time # Retorna o tempo atual em segundos desde a época
ctime # Converte o tempo em segundos para uma string legível
localtime # Converte o tempo em segundos para uma struct_time em UTC
strftime # Converte uma struct_time para uma string formatada   
    # Exemplo de uso
print("Iniciando...")
sleep(2)
print("Processando...")
sleep(2)
print("Finalizando...")
print("Pronto!")
print(time.ctime())
print(time.localtime())

import datetime # Importa toda a Biblioteca de data e hora
from datetime import datetime # Importa apenas o elemento "datetime", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "datetime"
datetime # Retorna a data e hora atual
date # Retorna a data atual
time # Retorna a hora atual
timedelta # Representa a diferença entre duas datas
    # Exemplo de uso
print(datetime.now())
print(date.today())
print(time())
print(timedelta(days=1))

import os # Importa toda a Biblioteca de sistema operacional
from os import system # Importa apenas o elemento "system", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "os"
system # Executa um comando do sistema operacional  
name # Retorna o nome do sistema operacional
getcwd # Retorna o diretório atual
listdir # Retorna a lista de arquivos e diretórios no diretório atual
    # Exemplo de uso
print(os.getcwd())
print(os.listdir())
print(os.name)
os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do terminal

import sys # Importa toda a Biblioteca de sistema
from sys import exit # Importa apenas o elemento "exit", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "sys"
exit # Encerra o programa   
version # Retorna a versão do Python
platform # Retorna a plataforma do sistema operacional
    # Exemplo de uso
print(sys.version)
print(sys.platform)
#sys.exit() # Encerra o programa

import requests # Importa toda a Biblioteca de requisições HTTP
from requests import get # Importa apenas o elemento "get", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "requests"
get # Realiza uma requisição GET
post # Realiza uma requisição POST
put # Realiza uma requisição PUT
delete # Realiza uma requisição DELETE
    # Exemplo de uso
response = get('https://api.github.com')
print(response.status_code)
print(response.json())
print(response.headers)

import json # Importa toda a Biblioteca de JSON
from json import loads # Importa apenas o elemento "loads", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "json"
loads # Converte uma string JSON em um objeto Python
dumps # Converte um objeto Python em uma string JSON
    # Exemplo de uso
data = '{"nome": "Ana", "idade": 25}'   
obj = json.loads(data)
print(obj['nome'])
print(json.dumps(obj))

import re # Importa toda a Biblioteca de expressões regulares
from re import match # Importa apenas o elemento "match", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "re"
match # Tenta encontrar uma correspondência com uma expressão regular
search # Tenta encontrar uma correspondência em qualquer lugar da string
findall # Retorna todas as correspondências em uma lista
sub # Substitui as correspondências por outra string
    # Exemplo de uso
texto = "O gato está em cima da mesa"
padrao = r"gato"
if re.match(padrao, texto):
    print("Encontrado no início da string")
if re.search(padrao, texto):
    print("Encontrado em algum lugar da string")
resultados = re.findall(padrao, texto)
print(resultados)
novo_texto = re.sub(padrao, "cachorro", texto)
print(novo_texto)

import pandas as pd # Importa toda a Biblioteca de análise de dados
from pandas import DataFrame # Importa apenas o elemento "DataFrame", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "pandas"
DataFrame # Cria um DataFrame a partir de dados
Series # Cria uma Series a partir de dados
read_csv # Lê um arquivo CSV e retorna um DataFrame
    # Exemplo de uso
df = pd.read_csv('dados.csv')
print(df.head())
print(df.describe())
print(df['coluna'].mean())

import numpy as np # Importa toda a Biblioteca de computação científica
from numpy import array # Importa apenas o elemento "array", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "numpy"
array # Cria um array a partir de uma lista
arange # Cria um array com valores em um intervalo
reshape # Altera a forma de um array
linspace # Cria um array com valores espaçados uniformemente em um intervalo
    # Exemplo de uso
arr = np.array([1, 2, 3, 4, 5])
print(arr.reshape(5, 1))
print(np.linspace(0, 1, 5))

import matplotlib.pyplot as plt # Importa toda a Biblioteca de plotagem de gráficos
from matplotlib.pyplot import plot # Importa apenas o elemento "plot", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "matplotlib.pyplot"
plot # Plota um gráfico de linhas   
scatter # Plota um gráfico de dispersão
bar # Plota um gráfico de barras
hist # Plota um histograma
    # Exemplo de uso
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.title("Gráfico de Linhas")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()
plt.scatter(x, y)
plt.title("Gráfico de Dispersão")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()
plt.bar(x, y)
plt.title("Gráfico de Barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()
plt.hist(y, bins=5)
plt.title("Histograma")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.show()

import seaborn as sns # Importa toda a Biblioteca de visualização de dados  
from seaborn import heatmap # Importa apenas o elemento "heatmap", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "seaborn"
heatmap # Plota um mapa de calor
pairplot # Plota gráficos de dispersão para todas as combinações de variáveis
distplot # Plota um histograma com uma curva de densidade
    # Exemplo de uso
import pandas as pd
df = pd.read_csv('dados.csv')
sns.heatmap(df.corr(), annot=True)
plt.show()
sns.pairplot(df)
plt.show()
sns.distplot(df['coluna'])
plt.show()

import tkinter as tk # Importa toda a Biblioteca de interface gráfica   
from tkinter import Tk # Importa apenas o elemento "Tk", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "tkinter"
Label # Cria um rótulo
Button # Cria um botão
Entry # Cria um campo de entrada
Text # Cria uma área de texto
    # Exemplo de uso
root = Tk()
root.title("Exemplo de Interface Gráfica")
label = Label(root, text="Digite seu nome:")
label.pack()
entry = Entry(root)
entry.pack()
button = Button(root, text="Enviar")
button.pack()
text = Text(root)
text.pack()
root.mainloop()

import sqlite3 # Importa toda a Biblioteca de banco de dados SQLite
from sqlite3 import connect # Importa apenas o elemento "connect", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "sqlite3"
Cursor # Cria um cursor para executar comandos SQL
execute # Executa um comando SQL
fetchall # Retorna todos os resultados de uma consulta
commit # Salva as alterações no banco de dados
    # Exemplo de uso
conn = connect('banco_de_dados.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM tabela')
resultados = cursor.fetchall()
print(resultados)
conn.commit()
conn.close()

import smtplib # Importa toda a Biblioteca de envio de e-mails
from smtplib import SMTP # Importa apenas o elemento "SMTP", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "smtplib"
SMTP # Cria um objeto SMTP para enviar e-mails
sendmail # Envia um e-mail
quit # Encerra a conexão com o servidor SMTP
    # Exemplo de uso
smtp = SMTP('smtp.exemplo.com')
smtp.login('usuario', 'senha')
smtp.sendmail('de@exemplo.com', 'para@exemplo.com', 'Olá, mundo!')
smtp.quit()

import ftplib # Importa toda a Biblioteca de FTP
from ftplib import FTP # Importa apenas o elemento "FTP", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "ftplib"
FTP # Cria um objeto FTP para se conectar a um servidor FTP
login # Faz login em um servidor FTP
cwd # Altera o diretório de trabalho
retrbinary # Faz o download de um arquivo em modo binário
    # Exemplo de uso
ftp = FTP('ftp.exemplo.com')
ftp.login('usuario', 'senha')
ftp.cwd('/diretorio')
ftp.retrbinary('RETR arquivo.txt', open('arquivo.txt', 'wb').write)
ftp.quit()

import smtplib # Importa toda a Biblioteca de envio de e-mails
from smtplib import SMTP # Importa apenas o elemento "SMTP", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "smtplib"
SMTP # Cria um objeto SMTP para enviar e-mails
sendmail # Envia um e-mail
quit # Encerra a conexão com o servidor SMTP
    # Exemplo de uso
smtp = SMTP('smtp.exemplo.com')
smtp.login('usuario', 'senha')
smtp.sendmail('de@exemplo.com', 'para@exemplo.com', 'Olá, mundo!')
smtp.quit()

import email # Importa toda a Biblioteca de manipulação de e-mails
from email import message_from_string # Importa apenas o elemento "message_from_string", ou seja, importa só o elemanto selecionado apos a tag Importe
    # Elementos da biblioteca "email"
message_from_string # Cria um objeto de mensagem a partir de uma string
email.message.EmailMessage # Cria um objeto de mensagem de e-mail
email.utils.make_msgid # Gera um ID único para a mensagem
    # Exemplo de uso
msg = email.message.EmailMessage()  
msg['Subject'] = 'Assunto'
msg['From'] = 'de@exemplo.com'
msg['To'] = 'para@exemplo.com'
msg.set_content('Olá, mundo!')
print(msg)
