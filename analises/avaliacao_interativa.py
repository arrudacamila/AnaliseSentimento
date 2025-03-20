from .sentimentoAnalise import analisar_sentimento

def main():
    while True:
        try:
            avaliacao = int(input("Digite uma avaliação numérica (1 a 5) ou 0 para sair: "))
            if avaliacao == 0:
                break
            elif 1 <= avaliacao <= 5:
                sentimento = analisar_sentimento(avaliacao)
                print(f'Avaliação: {avaliacao} - Sentimento: {sentimento}')
            else:
                print("Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == '__main__':