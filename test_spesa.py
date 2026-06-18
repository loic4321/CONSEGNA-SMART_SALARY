import unittest

from models.categoria import Categoria
from models.spesa import Spesa


class TestSpesa(unittest.TestCase):
    
    def test_spesa(self):
        
        categoria = Categoria(
            "Piacere",
            3,
            10
        )
        
        spesa = Spesa(
            "Cinema",
            50,
            categoria
        )
        
        self.assertEqual(
            spesa.importo,
            50
        )
        
        
if __name__ == '__main__':
    
    unittest.main()