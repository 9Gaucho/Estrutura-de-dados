def calcular_media(lista):
    soma = 0
    contador = 0
    for elemento in lista:
        soma += elemento
        contador += 1
    return soma / contador

def calcular_desvio_padrao(lista):
    soma = 0
    media = calcular_media(lista)
    contador = 0
    for elemento in lista:
        soma += (elemento - media) ** 2
        contador += 1
    variancia = soma / contador
    desvio_padrao = variancia ** 0.5
    return desvio_padrao

def onca_mais_velha(sexo, idades):
    indice = 0
    idade_max = idades[0]
    for i in range(1, len(idades)):
        if idades[i] > idade_max:
            idade_max = idades[i]
            indice = i
    return indice, idade_max

def onca_mais_nova(sexo, idades):
    indice = 0
    idade_min = idades[0]
    for i in range(1, len(idades)):
        if idades[i] < idade_min:
            idade_min = idades[i]
            indice = i
    return indice, idade_min

def onca_mais_pesada(sexo, pesos):
    indice = 0
    peso_max = pesos[0]
    for i in range(1, len(pesos)):
        if pesos[i] > peso_max:
            peso_max = pesos[i]
            indice = i
    return indice, peso_max

def onca_mais_leve(sexo, pesos):
    indice = 0
    peso_min = pesos[0]
    for i in range(1, len(pesos)):
        if pesos[i] < peso_min:
            peso_min = pesos[i]
            indice = i
    return indice, peso_min

arquivo = "oncas_pintadas.txt"
oncas_id = []
oncas_sexo = []
oncas_peso = []
oncas_idade = []

with open(arquivo, "r") as file:
    for linha in file:
        valores = linha.strip().split(",")
        oncas_id.append(int(valores[0]))
        oncas_sexo.append(valores[1])
        oncas_peso.append(float(valores[2]))
        oncas_idade.append(int(valores[3]))

# Separando os dados por sexo
pesos_machos = []
pesos_femeas = []
idades_machos = []
idades_femeas = []

for i in range(len(oncas_sexo)):
    if oncas_sexo[i] == "M":
        pesos_machos.append(oncas_peso[i])
        idades_machos.append(oncas_idade[i])
    elif oncas_sexo[i] == "F":
        pesos_femeas.append(oncas_peso[i])
        idades_femeas.append(oncas_idade[i])

# Média e desvio padrão dos pesos e idades por gênero
media_peso_machos = calcular_media(pesos_machos)
media_peso_femeas = calcular_media(pesos_femeas)
desvio_padrao_peso_machos = calcular_desvio_padrao(pesos_machos)
desvio_padrao_peso_femeas = calcular_desvio_padrao(pesos_femeas)
media_idade_machos = calcular_media(idades_machos)
media_idade_femeas = calcular_media(idades_femeas)
desvio_padrao_idade_machos = calcular_desvio_padrao(idades_machos)
desvio_padrao_idade_femeas = calcular_desvio_padrao(idades_femeas)

# Percentual de onças M e F
total_oncas = 0
total_machos = 0
total_femeas = 0

for sexo in oncas_sexo:
    total_oncas += 1
    if sexo == "M":
        total_machos += 1
    elif sexo == "F":
        total_femeas += 1

percentual_machos = (total_machos / total_oncas) * 100
percentual_femeas = (total_femeas / total_oncas) * 100

# Encontrar as características das onças
indice_mais_velha_macho, idade_mais_velha_macho = onca_mais_velha("M", idades_machos)
indice_mais_nova_macho, idade_mais_nova_macho = onca_mais_nova("M", idades_machos)
indice_mais_pesada_macho, peso_mais_pesada_macho = onca_mais_pesada("M", pesos_machos)
indice_mais_leve_macho, peso_mais_leve_macho = onca_mais_leve("M", pesos_machos)

indice_mais_velha_femea, idade_mais_velha_femea = onca_mais_velha("F", idades_femeas)
indice_mais_nova_femea, idade_mais_nova_femea = onca_mais_nova("F", idades_femeas)
indice_mais_pesada_femea, peso_mais_pesada_femea = onca_mais_pesada("F", pesos_femeas)
indice_mais_leve_femea, peso_mais_leve_femea = onca_mais_leve("F", pesos_femeas)

print("\033[92m" + "Análise das Onças Pintadas:" + "\033[0m")
print("----------------------------")
print("\033[94m" + "Média de peso (Machos):", media_peso_machos)
print("Desvio padrão de peso (Machos):", desvio_padrao_peso_machos)
print("\033[95m" + "Média de peso (Fêmeas):", media_peso_femeas)
print("Desvio padrão de peso (Fêmeas):", desvio_padrao_peso_femeas)
print("\033[94m" +"Média de idade (Machos):", media_idade_machos)
print("Desvio padrão de idade (Machos):", desvio_padrao_idade_machos)
print("\033[95m" + "Média de idade (Fêmeas):", media_idade_femeas)
print("Desvio padrão de idade (Fêmeas):", desvio_padrao_idade_femeas)
print("\033[94m" +"Percentual de Machos:", percentual_machos)
print("\033[95m" +"Percentual de Fêmeas:", percentual_femeas)

print("\033[94m" + "\nCaracterísticas das Onças Machos:" + "\033[0m")
print("----------------------------------")
print("Mais velha:", oncas_id[indice_mais_velha_macho], "com", idade_mais_velha_macho, "anos")
print("Mais nova:", oncas_id[indice_mais_nova_macho], "com", idade_mais_nova_macho, "anos")
print("Mais pesada:", oncas_id[indice_mais_pesada_macho], "com", peso_mais_pesada_macho, "kg")
print("Mais leve:", oncas_id[indice_mais_leve_macho], "com", peso_mais_leve_macho, "kg")

print("\033[95m" + "\nCaracterísticas das Onças Fêmeas:" + "\033[0m")
print("-----------------------------------")
print("Mais velha:", oncas_id[indice_mais_velha_femea], "com", idade_mais_velha_femea, "anos")
print("Mais nova:", oncas_id[indice_mais_nova_femea], "com", idade_mais_nova_femea, "anos")
print("Mais pesada:", oncas_id[indice_mais_pesada_femea], "com", peso_mais_pesada_femea, "kg")
print("Mais leve:", oncas_id[indice_mais_leve_femea], "com", peso_mais_leve_femea, "kg")


