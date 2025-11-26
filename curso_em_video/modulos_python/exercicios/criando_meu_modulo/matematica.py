import math as m
import random as r

def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def aleatorio(a,b):
    return r.randint(min(a,b), max(a,b))

def divisao(a,b):
    return a/b

def seno(a):
    return m.sin(a)

def cosseno(a):
    return m.cos(a)

def tangente(a):
    return m.tan(a)

def graus_para_radianos(graus):
    return m.radians(graus)