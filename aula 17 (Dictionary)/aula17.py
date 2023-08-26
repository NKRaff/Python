import os
os.system('cls')

# Dictionary
pc = {
    "Processador":"I5 3330",
    "Ram":"16Gb DDR3",
    "Placa de Video":"Gtx 1660 Super",
    "Gabinete":"Branco"
}

# Pegando um Valor atravez de uma Chave
cpu = pc.get("Processador")      #cpu = pc["Processador"]

# Modificando um Valor existente
pc["Gabinete"] = "Preto"

# Mostrando os Valores atravez das Chaves
print(f"""
Placa de Video: {pc['Placa de Video']}
Processador: {cpu}
Ram: {pc['Ram']}
Gabinete: {pc['Gabinete']}
""")

# Tamanho do Dictionary
print(f"Quantidade de peças: {len(pc)} \n")

# Condicional
if("Water Cooler" in pc):
    print("Computador tem water cooler! \n")
else:
    print("Computador não tem water cooler! \n")

# Adicionando nava Chave e Valor ao Dictionary
pc["Fan"] = 6

# Removendo uma Chave do Dictionary
pc.pop("Gabinete")              # del pc["Gabinete"]
                                # pc.clear()

# Printando o Dictionary por uma repetição
for x in pc:                    # for x,y in pc.items():
    print(f"{x}: {pc[x]}")      #    print(f"{x}: {y}")



os.system('cls')



pcs = {
    "Pc1":{
        "Processador":"I5 3330",
        "Ram":"16Gb DDR3",
        "Placa de Video":"Gtx 1660 Super"
    },
    "Pc2":{
        "Processador":"I3 2100",
        "Ram":"8Gb DDR3",
        "Placa de Video":"9800 GT"
    },
    "Pc3":{
        "Processador":"Celeron",
        "Ram":"3Gb DDR3"
    }
}

"""
Computador1 = {
    "Processador":"I5 3330",
    "Ram":"16Gb DDR3",
    "Placa de Video":"Gtx 1660 Super"
}
Computador2 = {
    "Processador":"I3 2100",
    "Ram":"8Gb DDR3",
    "Placa de Video":"9800 GT"
}
Computador3 = {
    "Processador":"Celeron",
    "Ram":"3Gb DDR3"
}

pcs = {
    "pc1": Computador1,
    "pc2": Computador2,
    "pc3": Computador3
}
"""

print(pcs["Pc1"]["Processador"])



