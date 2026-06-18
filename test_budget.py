import unittest

from models.budget import BudgetMensile


class TestBudget(unittest.TestCase):
    
    def test_creazione_budget(self):
        
        budget = BudgetMensile(
            2000
        )
        
        self.assertEqual(
            budget.stipendio,
            2000
        )
        
    def test_saldo_iniziale(self):
        
        budget = BudgetMensile(
            1500
        )
        
        self.assertEqual(
            budget.saldo,
            1500
        )
        
        
if __name__ == '__main__':
    
    unittest.main()