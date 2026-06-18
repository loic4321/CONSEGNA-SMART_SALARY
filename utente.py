class Utente:
    
    def __init__(
        self, 
        nome,
        email
    ):
        
        self.nome = nome
        
        self.email = email
        
        self.budget = None
        
    def assegna_budget(
        self,
        budget
    ):
        
        self.budget = budget
        
    def mostra_utente(self):
        
        return (
            f"Nome: {self.nome}  | "
            f"Email: {self.email}"
            
        )