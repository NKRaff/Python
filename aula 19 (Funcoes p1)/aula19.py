import os
os.system('cls')

num1 = 5; num2 = 10

def somar():
    print(f"{num1} + {num2} = {num1 + num2}")
def subtrair():
    print(f"{num1} - {num2} = {num1 - num2}")
def multiplicacao():
    print(f"{num1} x {num2} = {num1 * num2}")

def calculo():
    somar()
    subtrair()
    multiplicacao()

calculo()
