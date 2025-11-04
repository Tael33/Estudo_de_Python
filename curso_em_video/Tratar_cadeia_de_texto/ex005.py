# Faça umm programa que leia uma frase e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip().upper()
print(f'A frase tem {frase.count('A')} letras "A"')
print(f'A primeira letra "A" aparece na posição {frase.find('A') + 1}')
print(f'A última vez que a letra "A" aparece está na posição {frase.rfind("A") + 1}')