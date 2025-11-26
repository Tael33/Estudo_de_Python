import turtle

def desenhar_casa():
    
    # Configura a janela
    janela = turtle.Screen()
    janela.bgcolor("skyblue")

    # Cria e configura a tartaruga
    casa = turtle.Turtle()
    casa.speed(0)  # Define a velocidade para a mais rápida
    casa.hideturtle()

    # --- Desenha a base da casa (quadrado) ---
    casa.penup()
    casa.goto(-100, -120)
    casa.pendown()
    casa.fillcolor("wheat")

    casa.begin_fill()
    for _ in range(4): # Desenha um quadrado
        casa.forward(200)
        casa.left(90)
    casa.end_fill()

    # --- Desenha o telhado (triângulo) ---
    casa.penup()
    casa.goto(-100, 80)
    casa.pendown()
    casa.fillcolor("firebrick")

    # Desenha um triângulo
    casa.begin_fill()
    for _ in range(3): 
        casa.forward(200)
        casa.left(120)
    casa.end_fill()

    # --- Desenha a porta (retângulo) ---
    casa.penup()
    casa.goto(-25, -120)
    casa.pendown()
    casa.fillcolor("saddlebrown")
    
    casa.begin_fill()
    for _ in range(2): # Desenha um retângulo
        casa.forward(50)
        casa.left(90)
        casa.forward(90)
        casa.left(90)
    casa.end_fill()

    # --- Desenha a janela (quadrado) ---
    casa.penup()
    casa.goto(-25, -20)
    casa.pendown()
    casa.fillcolor("lightblue")

    casa.begin_fill()
    for _ in range(4): # Desenha um quadrado
        casa.forward(50)
        casa.left(90)
    casa.end_fill()

    janela.exitonclick() # Mantém a janela aberta até um clique na tela

# Chama a função para iniciar o desenho
desenhar_casa()
