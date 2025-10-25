
# open("caminho", "modo", encoding = 'UTF-8')

# Modos

# r - Leitura
# a - Append / Incrementar
# w - Escrita - se usado em um arquivo existente ele apaga tudo o que estava antes/ se o arquivo não existir ele cria e escreve
# x - Criar Arquivo
# r+ - Leitura + Escrita

# Funções

# .close() - fecha o arquivo aberto. OBSERVASÃO: Sepre use esse comando ao final do código.
# .readable() - Verifica se o arquivo pode ser lido. Retorna true ou false
# .read() - ler/Abre o arquivo.
# .readline() - ler/Abre uma lina 'Primeira linha'
# .readlines() - ler/ transforma linha por lina em uma lista
# .write() - Escreve no arquivo no final/Ultima linha, mas colado ao ultimo texto. Para quebrar linha basta usar \n Ex: .write("\n Texto a ser atribuido")

# para remover arquivo no python tem que usar uma biblioteca chamada 'OS'

# import os

# os.remove("") - remove pelo caminho do arquivo
# os.path.exists("") - verifica se existe o arquivo pelo caminho
# os.rmdir("") - remove pasta se tiver vazia

# arquivo = open('manipulação_de_arquivos/teste.txt', 'a')

# #arquivo.readable()
# #print(arquivo.read())

# arquivo.close()

with open('teste.txt', 'r', encoding = 'UTF-8') as arq:
    
    print(arq.readable())