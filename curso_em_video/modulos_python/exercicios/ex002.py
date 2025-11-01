# Façã um programa que abra e reproduza um áudio de arquivo
# mp3

import pygame

# Iniciar a biblioteca
pygame.init()

# Abrir o arquivo
pygame.mixer.music.load()

# Rodar o arquivo
pygame.mixer.music.play()

# Esperar o arquivo finalizar para Fechar
pygame.event.wait()