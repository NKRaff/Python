import os
os.system('cls')

def concatenar(num1, num2):
    print(f"{num1} + {num2} = {num1}{num2}\n")

def fun(*n):
    for x in n:
        print(x)

def multiplicar(*n):
    r = 1
    for x in n:
        r *= x
    print(f"Multiplicação = {r}")

var = [2, 5, 8, 3, 1]
def somar(num):
    r = 0
    for x in num:
        r += x
    print(f"Soma: {r}\n")


def linguagem(l = "Python"):
    print(f"\nLinguagem: {l}\n")

concatenar(4, 9)
fun("Python", "Java", "PHP", "Javascript", "Ruby\n")
multiplicar(2, 5, 6, 1, 8)
linguagem("Javascript")
somar(var)
