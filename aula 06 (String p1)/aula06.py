# Uma string é um array de caracteres

var = "Teste"

# A função strip remove espaços vazios no inicio e no fim da variavel
# A função lower deixa toda a string minuscula
# A função upper deixa toda a string maiuscula
# A função replace substitui uma string por outra string
# A função split separa a string em arrays

print("Variavel: " + var.strip())
print("Variavel minuscula: " + var.lower())
print("Variavel maiuscula: " + var.upper())
print("Variavel modificada: " + var.replace("Teste", "Teste 02"))
print("Variavel Splitada: " + str(var.split("e")))
print("Letra especifica: " + var[0])
print("Intervalo especifico: " + var[1:3])
print("Tamanho: " + str(len(var)))