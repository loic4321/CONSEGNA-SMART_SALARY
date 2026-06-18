class BudgetMensile:
    
    def __init__(self, stipendio):
        
        self.stipendio = stipendio
        
        self.saldo = stipendio
        
        self.categorie = []
        
        self.fondi = []
        
        self.spese = []
        
    def aggiungi_categoria(
        self,
        categoria
    ):
        
        
        self.categorie.append(
            categoria
        )
        
    def aggiungi_fondo(
        self,
        fondo
    ):
        
        
        self.fondi.append(
            fondo
        )
        
    def aggiungi_spesa(
        self,
        spesa
    ):
        
        
        self.spese.append(
            spesa
        )
        
        self.saldo -= (
            spesa.importo
        )
        
    def mostra_budget(self):
        
        return (
            f"Stipendio: "
            f"{self.stipendio}€  | "
            f"Saldo: "
            f"{self.saldo}€"
        )

    