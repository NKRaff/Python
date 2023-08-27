import os
os.system('cls')

var = [2, 5, 8, 3, 1, 1]
def somar(num):
    r = 0
    for x in num:
        r += x
    return r

resultado = somar(var)
for x in var:
    print(f"{x} + ", end="")

print(f"= {resultado}")
if(resultado % 2 == 0):
    print("Numero Par!\n")
else:
    print("Numero Impar!\n")
