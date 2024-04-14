# Função para calcular a média de uma lista de números
def calcular_media(lista):
    return sum(lista) / len(lista)

# Função para calcular o desvio padrão de uma lista de números
def calcular_desvio_padrao(lista):
    media = calcular_media(lista)
    variancia = sum((x - media) ** 2 for x in lista) / len(lista)
    desvio_padrao = variancia ** 0.5
    return desvio_padrao

# Função para encontrar a onça mais velha
def onca_mais_velha(sexo, idades):
    indice = idades.index(max(idades))
    return indice, idades[indice]

# Função para encontrar a onça mais nova
def onca_mais_nova(sexo, idades):
    indice = idades.index(min(idades))
    return indice, idades[indice]

# Função para encontrar a onça mais pesada
def onca_mais_pesada(sexo, pesos):
    indice = pesos.index(max(pesos))
    return indice, pesos[indice]

# Função para encontrar a onça mais leve
def onca_mais_leve(sexo, pesos):
    indice = pesos.index(min(pesos)) 
    return indice, pesos[indice]

# Abrindo o arquivo e lendo os dados
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
pesos_machos = [oncas_peso[i] for i in range(len(oncas_peso)) if oncas_sexo[i] == "M"]
pesos_femeas = [oncas_peso[i] for i in range(len(oncas_peso)) if oncas_sexo[i] == "F"]
idades_machos = [oncas_idade[i] for i in range(len(oncas_idade)) if oncas_sexo[i] == "M"]
idades_femeas = [oncas_idade[i] for i in range(len(oncas_idade)) if oncas_sexo[i] == "F"]

# Calcular média e desvio padrão dos pesos e idades por gênero
media_peso_machos = calcular_media(pesos_machos)
media_peso_femeas = calcular_media(pesos_femeas)
desvio_padrao_peso_machos = calcular_desvio_padrao(pesos_machos)
desvio_padrao_peso_femeas = calcular_desvio_padrao(pesos_femeas)
media_idade_machos = calcular_media(idades_machos)
media_idade_femeas = calcular_media(idades_femeas)
desvio_padrao_idade_machos = calcular_desvio_padrao(idades_machos)
desvio_padrao_idade_femeas = calcular_desvio_padrao(idades_femeas)

# Calcular percentual de onças machos e fêmeas
percentual_machos = len(pesos_machos) / len(oncas_id) * 100
percentual_femeas = len(pesos_femeas) / len(oncas_id) * 100

# Encontrar as características das onças de cada gênero
indice_mais_velha_macho, idade_mais_velha_macho = onca_mais_velha("M", idades_machos)
indice_mais_nova_macho, idade_mais_nova_macho = onca_mais_nova("M", idades_machos)
indice_mais_pesada_macho, peso_mais_pesada_macho = onca_mais_pesada("M", pesos_machos)
indice_mais_leve_macho, peso_mais_leve_macho = onca_mais_leve("M", pesos_machos)

indice_mais_velha_femea, idade_mais_velha_femea = onca_mais_velha("F", idades_femeas)
indice_mais_nova_femea, idade_mais_nova_femea = onca_mais_nova("F", idades_femeas)
indice_mais_pesada_femea, peso_mais_pesada_femea = onca_mais_pesada("F", pesos_femeas)
indice_mais_leve_femea, peso_mais_leve_femea = onca_mais_leve("F", pesos_femeas)

print("Análise das Onças-Pintadas:")
print("----------------------------")
print("Média de peso (Machos):", media_peso_machos)
print("Desvio padrão de peso (Machos):", desvio_padrao_peso_machos)
print("Média de peso (Fêmeas):", media_peso_femeas)
print("Desvio padrão de peso (Fêmeas):", desvio_padrao_peso_femeas)
print("Média de idade (Machos):", media_idade_machos)
print("Desvio padrão de idade (Machos):", desvio_padrao_idade_machos)
print("Média de idade (Fêmeas):", media_idade_femeas)
print("Desvio padrão de idade (Fêmeas):", desvio_padrao_idade_femeas)
print("Percentual de Machos:", percentual_machos)
print("Percentual de Fêmeas:", percentual_femeas)

print("\nCaracterísticas das Onças-Machos:")
print("----------------------------------")
print("Mais velha:", oncas_id[indice_mais_velha_macho], "com", idade_mais_velha_macho, "anos")
print("Mais nova:", oncas_id[indice_mais_nova_macho], "com", idade_mais_nova_macho, "anos")
print("Mais pesada:", oncas_id[indice_mais_pesada_macho], "com", peso_mais_pesada_macho, "kg")
print("Mais leve:", oncas_id[indice_mais_leve_macho], "com", peso_mais_leve_macho, "kg")

print("\nCaracterísticas das Onças-Fêmeas:")
print("-----------------------------------")
print("Mais velha:", oncas_id[indice_mais_velha_femea], "com", idade_mais_velha_femea, "anos")
print("Mais nova:", oncas_id[indice_mais_nova_femea], "com", idade_mais_nova_femea, "anos")
print("Mais pesada:", oncas_id[indice_mais_pesada_femea], "com", peso_mais_pesada_femea, "kg")
print("Mais leve:", oncas_id[indice_mais_leve_femea], "com", peso_mais_leve_femea, "kg")
