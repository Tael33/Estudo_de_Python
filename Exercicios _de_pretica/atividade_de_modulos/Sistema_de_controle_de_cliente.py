def criar_arquivo(nome_arq):
    with open (nome_arq, 'x', encoding='utf-8') as arquivo:
        arquivo.write('')
    

# Formato de dados de cada linha 'Nome|Email|Telefone

# validade se o nome completo 
def validar_nm():
    
    while True:
        valido = True
        nome = input('Digite o seu nome: ').strip().title()
        for caracter in nome:
            if caracter.isnumeric():
                valido = False
                break
        if valido == True:
            break
        else:
            print('Nome inválido')        
    return nome


def validar_email():
    
    while True:
        email = input('Digite o seu email: ').strip()
        if '@' in email and '.' in email:
            break
        else:
            print('Email inválido')
    return email


def validar_telefone():
    
    while True:
        telefone = input("Digite o seu telefone 'sem () ou -': ").strip()
        if telefone.isnumeric() and len(telefone) == 8:
            break
        else:
            print('Telefone inválido')
    return telefone

def valiar(nome, email, telefone):
    return f'{nome} | {email} | {telefone}'

def gravar_arq(nome_arq, dados):
    with open(nome_arq, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{dados}\n')
        
def ler_arq(nome_arq):
    with open(nome_arq, 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())


def menu():
    opcao = (input('Qual a sua opção: '))
    return opcao


print('''

Menu de Opções:
      Opção !: Criar um novo!
      Opção 1: Inserir Dados!
      Opção 2: #############
      Opção 3: #############
      Opção 4: Sair!
''')

while True:
    opcao = menu()
    if opcao == "4":
        break
    elif opcao == '!':
        nomeArquivo = input('Qual o nome do arquivo: ')

        criar_arquivo(nomeArquivo)
    elif opcao == '1':
        nome = validar_nm()
        email = validar_email()
        telefone = validar_telefone()
        dados = valiar(nome, email, telefone)

        nomeArquivo = input('Qual o nome do arquivo: ')

        gravar_arq(nomeArquivo, dados)
        print('Dados gravados com sucesso!')
        ler_arq(nomeArquivo)
        
    elif opcao == "2" or opcao == "3":
        print('Essa opção está em andamento!')
    else:
        print('Erro tente novamente!')