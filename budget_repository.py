class BudgetRepository:

    def __init__(self):

        self.budget_salvato = None

    def salva_budget(
        self,
        budget
    ):

        self.budget_salvato = budget

    def carica_budget(self):

        return self.budget_salvato