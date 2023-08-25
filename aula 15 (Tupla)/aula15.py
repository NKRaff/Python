import os
os.system('cls')

#lVar = ["Python", "Java", "PHP"] <- é uma lista
#tVar = ("Python", "Java", "PHP") <- é uma tupla

# Não se pode adicionar ou modificar uma tupla

tVar = ("Python", "Java", "PHP")
lvar = list(tVar)

lvar[1] = "Javascript"
tVar = tuple(lvar)

for x in tVar:
    print(x)
