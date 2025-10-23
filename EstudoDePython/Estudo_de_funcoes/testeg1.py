estoque_sangue = [['O+', 35],['A+', 28],['B-', 8],['AB+', 5],['O-', 12],['A-', 6], ['B+', 15]]

def validar_acesso():
    outorizados = ['HEMO-101', 'HEMO-25B', 'LAB-44C']
    
    while True:

        codigo = input('Digite seu código: ').upper().strip().split()
        codigo_novo = ''.join(codigo)
        
        if codigo_novo in outorizados:
            print('Acesso Permitido!')
            return True
        else:
            print('Acesso negado! Tente novamente.')

validar_acesso()