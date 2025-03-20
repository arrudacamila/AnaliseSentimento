#O arquivo utils.py pode ser utilizado para organizar funções auxiliares que você venha a utilizar, 
# como a limpeza de texto ou manipulação de entradas. 
# Mesmo que você ainda não tenha funções auxiliares, é bom deixar o arquivo pronto.
#No momento, ele pode ficar vazio ou, caso queira adicionar uma função simples de 
# limpeza de texto (como remover espaços extras), coloque o seguinte código:

# utils.py - Para funções auxiliares

def clean_text(text):
    """ Função para limpar texto, removendo espaços extras. """
    return " ".join(text.split())
