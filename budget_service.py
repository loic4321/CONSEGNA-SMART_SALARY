from models.budget import BudgetMensile

class BudgetService:
    
    def crea_budget(
        self,
        stipendio
    ):

        return BudgetMensile(
            stipendio
        )
        
    def aggiungi_categoria(
        self,
        budget,
        categoria
    ):

        budget.aggiungi_categoria(
            categoria
        )
        
    def aggiungi_spesa(
        self,
        budget,
        spesa
    ):

        budget.aggiungi_spesa(
            spesa
        )