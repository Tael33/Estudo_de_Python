'''crie umprograma que leia o nome completo de uma pessoa e verifique se tem "Silva" no nome'''

nome = input('Qualm o seu nome completo:').title().strip()

if 'Silva' in nome:
    print('Seu nome tem "Silva"')
else:
    print("Seu nome não tem 'Silva.'")