import unittest

class TestEventos(unittest.TestCase):

    def test_eventos_nao_vazios(self):
        eventos = ["Evento 1", "Evento 2"]
        self.assertGreater(len(eventos), 0) 

if __name__ == '__main__':
    unittest.main()
