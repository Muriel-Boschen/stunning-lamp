import unittest
from datetime import datetime

class TestData(unittest.TestCase):

    def test_data_hoje_formatada(self):
        data_hoje = datetime.today().strftime('%Y-%m-%d')
        self.assertEqual(len(data_hoje), 10)  

if __name__ == '__main__':
    unittest.main()
