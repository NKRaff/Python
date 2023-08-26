import random
import os
os.system('cls')

numRandom = random.randrange(1, 100)
tentativas = 0

while(True):
    num = int(input("Digite um número: "))
    if(num == numRandom):
        tentativas+=1
        break
    elif(num > numRandom):
        os.system('cls')
        print("Menor")
        tentativas+=1
    elif(num < numRandom):
        os.system('cls')
        print("Maior")
        tentativas+=1
    else:
        tentativas+=1

os.system('cls')

print("Acertou!")
print(f"O numero era: {numRandom}")
print(f"Numero de tentativas: {tentativas}")
