import unittest
from analises.sentimentoAnalise import analisar_sentimento

class TestSentimentoAnalise(unittest.TestCase):

    def test_positivo(self):
        self.assertEqual(analisar_sentimento(5), 'Positivo')
        self.assertEqual(analisar_sentimento(4), 'Positivo')

    def test_neutro(self):
        self.assertEqual(analisar_sentimento(3), 'Neutro')

    def test_negativo(self):
        self.assertEqual(analisar_sentimento(2), 'Negativo')
        self.assertEqual(analisar_sentimento(1), 'Negativo')

if __name__ == '__main__':
    unittest.main()