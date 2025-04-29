import unittest
from datetime import datetime
from scraper_wikipedia import get_eventos, format_data

class TestScraper(unittest.TestCase):

    def test_format_data(self):
        data_hoje = datetime.today().strftime('%Y-%m-%d')
        self.assertEqual(format_data(), data_hoje)

    def test_get_eventos_not_empty(self):
        eventos = get_eventos()
        self.assertGreater(len(eventos), 0)

    def test_get_eventos_type(self):
        eventos = get_eventos()
        self.assertIsInstance(eventos, list)

    def test_evento_format(self):
        eventos = get_eventos()
        for evento in eventos:
            self.assertIsInstance(evento, str)

    def test_eventos_have_content(self):
        eventos = get_eventos()
        for evento in eventos:
            self.assertGreater(len(evento), 5)
