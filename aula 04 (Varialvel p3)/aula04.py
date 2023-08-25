var = 1 #int
var = "texto" #string
var = 1.0 #float
var = False #boolean (1º letra maiuscula)

n1 = 5; n2 = 2; var = complex(n1, n2) # complexos

var = ["Python", "Java", "PHP", 1, 1.2, True] # ArrayList
var = ("Python", "Java", "PHP", 1, 1.2, True) # Tupla (não pode adicionar mais valores)
var = range(1, 100) # ArrayList (0-99)
var = { # Dectionary
    "nome": "Maria",
    "idade": 20
}
var = {1, 2, 2, 4, 5, 6, 6, 6, 7, 9, "roxo", "roxo"} # set (não repete valores)

# str() faz uma conversão forçada de um numero para uma string
print("Valor: " + str(var))
print("Tipo: "+ str(type(var)))

# print(var.real) #Real
# print(var.imag) #Imaginario

# print(var[2]) #[0 = Python, 1 = Java, 2 = PHP]

# print(var["nome"])