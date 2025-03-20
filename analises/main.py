from analises.sentimentoAnalise import analisar_sentimento

avaliacoes = [5, 3, 1, 4, 2]

for avaliacao in avaliacoes:
    sentimento = analisar_sentimento(avaliacao)
    print(f'Avaliação: {avaliacao} - Sentimento: {sentimento}')