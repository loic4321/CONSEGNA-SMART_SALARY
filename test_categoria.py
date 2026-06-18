import unittest

from models.categoria import Categoria


class TestCategoria(unittest.TestCase):
    
    def test_categoria(self):
        
        categoria = Categoria(
            "piacere",
            3,
            10
        )
        
        self.assertEqual(
            categoria.nome,
            "piacere"
        )
        
        self.assertEqual(
            categoria.percentuale,
            10
        )
        
        
if __name__ == '__main__':
    
    unittest.main()