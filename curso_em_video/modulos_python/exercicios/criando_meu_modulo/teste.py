import matematica as m

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"A soma de {num1} e {num2} é {m.soma(num1, num2)}")

print(f"A subtração de {num1} e {num2} é {m.subtracao(num1, num2)}")
print(f"A multiplicação de {num1} e {num2} é {m.multiplicar(num1, num2)}")
print(f"A divisão de {num1} e {num2} é {m.divisao(num1, num2):.2f}")

print(f"Um número aleatório entre {num1} e {num2} é {m.aleatorio(int(num1), int(num2))}")


angulo_graus = float(input("Digite um ângulo em GRAUS: "))

angulo_radianos = m.graus_para_radianos(angulo_graus)


print(f"O seno de {angulo_graus}° é {m.seno(angulo_radianos):.2f}")
print(f"O cosseno de {angulo_graus}° é {m.cosseno(angulo_radianos):.2f}")
print(f"A tangente de {angulo_graus}° é {m.tangente(angulo_radianos):.2f}")












