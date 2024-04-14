import urllib.request
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

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

# Função para baixar o arquivo e realizar a leitura dos dados, gerando as listas
def ler_dados_oncas_pintadas(url_arquivo):
    oncas_id = []
    oncas_sexo = []
    oncas_peso = []
    oncas_idade = []

    # Baixar o arquivo
    try:
        urllib.request.urlretrieve(url_arquivo, "oncas_pintadas.txt")
    except Exception as e:
        print("Erro ao baixar o arquivo:", e)
        return None, None, None, None

    # Ler os dados do arquivo baixado
    with open("oncas_pintadas.txt", "r") as file:
        for linha in file:
            valores = linha.strip().split(",")
            oncas_id.append(int(valores[0]))
            oncas_sexo.append(valores[1])
            oncas_peso.append(float(valores[2]))
            oncas_idade.append(int(valores[3]))

    return oncas_id, oncas_sexo, oncas_peso, oncas_idade

# Função para gerar o PDF com os resultados dos cálculos
def gerar_pdf_resultados(oncas_id, oncas_sexo, oncas_peso, oncas_idade):
    # Criar o documento PDF
    doc = SimpleDocTemplate("resultados_oncas_pintadas.pdf", pagesize=letter)
    
    # Criar uma lista para armazenar os dados tabulares
    data = []

    # Adicionar cabeçalhos
    data.append(["Métrica", "Machos", "Fêmeas"])

    # Calcular as métricas
    media_peso_machos = calcular_media([peso for peso, sexo in zip(oncas_peso, oncas_sexo) if sexo == "M"])
    media_peso_femeas = calcular_media([peso for peso, sexo in zip(oncas_peso, oncas_sexo) if sexo == "F"])
    desvio_padrao_peso_machos = calcular_desvio_padrao([peso for peso, sexo in zip(oncas_peso, oncas_sexo) if sexo == "M"])
    desvio_padrao_peso_femeas = calcular_desvio_padrao([peso for peso, sexo in zip(oncas_peso, oncas_sexo) if sexo == "F"])
    media_idade_machos = calcular_media([idade for idade, sexo in zip(oncas_idade, oncas_sexo) if sexo == "M"])
    media_idade_femeas = calcular_media([idade for idade, sexo in zip(oncas_idade, oncas_sexo) if sexo == "F"])
    desvio_padrao_idade_machos = calcular_desvio_padrao([idade for idade, sexo in zip(oncas_idade, oncas_sexo) if sexo == "M"])
    desvio_padrao_idade_femeas = calcular_desvio_padrao([idade for idade, sexo in zip(oncas_idade, oncas_sexo) if sexo == "F"])
    percentual_machos = (oncas_sexo.count("M") / len(oncas_sexo)) * 100
    percentual_femeas = (oncas_sexo.count("F") / len(oncas_sexo)) * 100
    
    # Adicionar métricas à lista de dados
    data.append(["Média de peso", f"{media_peso_machos:.2f} kg", f"{media_peso_femeas:.2f} kg"])
    data.append(["Desvio padrão de peso", f"{desvio_padrao_peso_machos:.2f} kg", f"{desvio_padrao_peso_femeas:.2f} kg"])
    data.append(["Média de idade", f"{media_idade_machos:.2f} anos", f"{media_idade_femeas:.2f} anos"])
    data.append(["Desvio padrão de idade", f"{desvio_padrao_idade_machos:.2f} anos", f"{desvio_padrao_idade_femeas:.2f} anos"])
    data.append(["Percentual de Machos", f"{percentual_machos:.2f}%", f"{percentual_femeas:.2f}%"])
    
    # Criar a tabela com os dados
    table = Table(data)

    # Adicionar estilo à tabela
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Aplicar estilo à tabela
    table.setStyle(style)

    # Adicionar tabela ao documento
    elements = [table]

    # Gerar o PDF
    doc.build(elements)
    print("PDF gerado com sucesso!")

# URL do arquivo de dados
url_arquivo = https://github.com/9Gaucho/Estrutura-de-dados/blob/main/oncas_pintadas.txt

# Ler os dados das onças pintadas
oncas_id, oncas_sexo, oncas_peso, oncas_idade = ler_dados_oncas_pintadas(url_arquivo)

# Verificar se os dados foram lidos corretamente
if oncas_id is not None:
    # Gerar o PDF com os resultados dos cálculos
    gerar_pdf_resultados(oncas_id, oncas_sexo, oncas_peso, oncas_idade)
else:
    print("Não foi possível ler os dados. Verifique a URL do arquivo.")
