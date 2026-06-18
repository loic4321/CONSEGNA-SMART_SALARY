class Spesa:
    def __init__(
        self,
        nome,
        importo,
        categoria
    ):
        
        self.nome = nome
        self.importo = importo
        self.categoria = categoria
        
    def mostra_spesa(self):
        
        
        return (
            f"{self.nome}  | "
            f"{self.importo}€  | "
            f"{self.categoria.nome}"
        )