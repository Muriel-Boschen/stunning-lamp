import unittest

class TestBasico(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(2 + 2, 4)

    def test_verdade(self):
        self.assertTrue(True)

    def test_texto(self):
        self.assertEqual("devops".upper(), "DEVOPS")
