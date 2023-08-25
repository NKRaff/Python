# O metodo append adiciona um elemento a lista
# O metodo remove remove um elemento do array
# O metodo pop remove o ultimo elemento do array
# O del remove o elemento no indece do array
# O metodo clear remove todos os elementos da lista

var = ["Java", "Python", "PHP"]
linguaguens = list(var)

var[0] = "JavaScript"

var.append("Java") #add apenas 1
var.remove("PHP") #var.remove(var[0])
var.pop()
del var[0]
var.clear()

print("Posições no Array: " + str(len(var)))
print("Lista: " + str(var))

print("Tamanho Array Inicial: " + str(len(linguaguens)))
print("Array Inicial: " + str(linguaguens))
