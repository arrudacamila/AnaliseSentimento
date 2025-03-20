#Esse será o arquivo principal que realiza a análise de sentimentos. 
# Como já discutido, você vai utilizar o VADER do nltk para analisar o sentimento do texto. 
# O código que você precisa colocar neste arquivo é o seguinte:

def analisar_sentimento(avaliacao):
    """
    Analisa o sentimento com base em uma avaliação numérica.
    
    Parâmetros:
    avaliacao (int): Avaliação numérica (por exemplo, de 1 a 5 estrelas)
    
    Retorna:
    str: Sentimento ('Positivo', 'Negativo' ou 'Neutro')
    """
    if avaliacao >= 4:
        return 'Positivo'
    elif avaliacao == 3:
        return 'Neutro'
    else:
        return 'Negativo'
