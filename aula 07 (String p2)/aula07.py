var = "Teste"
x = "String"

# O in/not in verifica se existe ou não na string

res = x not in var
res = x + " " +  var
print(res)

# O metodo format troca os "{}", por alguma string/variavel 
# Caracter de escape \ (barra invertida)
  # \n -> Quebra de linha
  # \" -> Adiciona aspas duplas
  # \' -> Adiciona aspas simples
  # \r -> 
  # \b -> Backspace
  # \t -> Tab

semana = "Quinta-feira"
dia = 10
mes = "agosto"
ano = 2023
data = "{},\n{} de \b{} de {}"
print(data.format(semana, dia, mes, ano))
