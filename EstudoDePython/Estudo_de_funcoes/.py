def validar(usuario, senha):
    retorno = []
    if usuario:
        resultado = []
        usuario_format = usuario.strip().split()
        novo_usuario = ''.join(usuario_format)
        valor = True
        resultado.append(novo_usuario)
        resultado.append(valor)
        retorno.append(resultado)
    if senha:
        resultado = []
        senha_format = senha.strip().split()
        nova_senha = ''.join(senha_format)
        
        if len(nova_senha) >= 6:
            valor = True
        else:
            valor = False
        resultado.append(nova_senha)
        resultado.append(valor)
        retorno.append(resultado)
    return retorno

while True:
    usuario = input("Digite o seu nome de usuário: ")
    senha = input("Digite sua senha com no mínimo 6 caracteres: ")

    retorno_validacao = validar(usuario, senha)

    valicacao = True

    if len(retorno_validacao) < 2:
        print("\nERRO: Usuário e senha não podem ser vazios. Tente novamente.\n")
        validacao = False
    for item in retorno_validacao:
        
        nome_campo = item[0]
        statos_campo = item[1]
        
        if nome_campo and statos_campo:
            print(f"Campo: {nome_campo}, 'Válido';")
        else:
            print(f"Campo: {nome_campo} 'Inválido'; Tente novamente.\n")
            validacao = False

    if valicacao:
        print("\n✅ Usuário e senha validados com sucesso!\n")
        break
    else:
        print("\n❌ Dados inválidos. Por favor, digite novamente.\n")