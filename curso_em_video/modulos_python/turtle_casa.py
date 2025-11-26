import turtle as tt

def criar_window():
    
    janela = tt.Screen()
    janela.bgcolor("skyblue")

    casa = tt.Turtle()
    casa.speed(0)  
    casa.hideturtle()

    return janela, casa

def desenhar_casa():
    
    janela, casa = criar_window()

    casa.penup()
    casa.goto(-100, -120)
    casa.pendown()
    casa.fillcolor("wheat")

    casa.begin_fill()
    for _ in range(4): 
        casa.forward(200)
        casa.left(90)
    casa.end_fill()




    janela.exitonclick()


desenhar_casa()