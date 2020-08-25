'''
Estas funções calculam o Bháskara após o usuário
inserir três valores numéricos.
'''

import math

def main():
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))
    c = float(input("Entre com o valor de c: "))
    imprime_raizes(a, b, c)
    
def delta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

def imprime_raizes(a,b,c):
    d = delta (a, b, c)
    if (d < 0):
        print("Esta equação não possui raízes reais.")
    else:
        if d == 0:
            raiz1 = -b / (2*a)
            print("A raiz desta equação é",raiz1,".")
        else:
            raiz1 = (-b + math.sqrt(d))/ 2*a
            raiz2 = (-b - math.sqrt(d))/ 2*a
            if raiz1 > raiz2:
                print("As raízes da equação são %.3f e %.3f."% (raiz2,raiz1))
            else:
                print("As raízes da equação são %.3f e %.3f."% (raiz1,raiz2))
