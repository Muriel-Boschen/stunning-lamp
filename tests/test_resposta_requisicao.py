import unittest
from unittest.mock import patch
import requests

class TestRequisicao(unittest.TestCase):

    @patch('requests.get')
    def test_resposta_requisicao(self, mock_get):
        mock_get.return_value.status_code = 200
        response = requests.get('https://pt.wikipedia.org/wiki/Portal:Eventos_atuais')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
