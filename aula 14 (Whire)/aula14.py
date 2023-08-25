import os
os.system('cls')

lista = []
linguagem = input("Digite o nome da linguagem: ")

while (linguagem != "0"):
    lista.append(linguagem)
    linguagem = input("Digite o nome da linguagem: ")

os.system('cls')
for i in lista:
    print("Linguagem: " + i)
