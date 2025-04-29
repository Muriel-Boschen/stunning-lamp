import unittest
from unittest.mock import patch
from scraper_wikipedia import scraper_function  
class TestScraper(unittest.TestCase):

    @patch('requests.get')
    def test_scraper_extraindo_eventos(self, mock_get):
        mock_get.return_value.text = "<html><body><ul><li>Evento 1</li><li>Evento 2</li></ul></body></html>"
        
        eventos = scraper_function('https://pt.wikipedia.org/wiki/Portal:Eventos_atuais')  
        self.assertEqual(len(eventos), 2)
        self.assertIn('Evento 1', eventos)
        self.assertIn('Evento 2', eventos)

if __name__ == '__main__':
    unittest.main()
