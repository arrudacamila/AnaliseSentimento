from flask import Flask, request, jsonify
from analises.sentimentoAnalise import analisar_sentimento

app = Flask(__name__)

@app.route('/analisar', methods=['POST'])
def analisar():
    data = request.get_json()
    avaliacao = data.get('avaliacao')
    if avaliacao is None or not (1 <= avaliacao <= 5):
        return jsonify({'error': 'Avaliação deve ser um número entre 1 e 5'}), 400

    sentimento = analisar_sentimento(avaliacao)
    return jsonify({'avaliacao': avaliacao, 'sentimento': sentimento})

if __name__ == '__main__':
    app.run(debug=True)