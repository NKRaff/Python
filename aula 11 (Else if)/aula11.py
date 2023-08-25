# elif é uma abreviação de else if

var1 = True
var2 = 10
var3 = "Verdadeiro"

print("Bloco do var1: ")
if var1:
    print("Verdadeiro")
else:
    print("Falso")

print("Bloco do var2")
if var2 > 0:
    print("Positivo")
elif var2 < 0:
    print("Negativo")
else:
    print("Nulo")

print("Bloco do var3")
if var3 == "Verdadeiro":
    print("Verdadeiro")
else:
    print("Falso")