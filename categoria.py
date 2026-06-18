class Categoria:

    def __init__(self, nome, priorita, percentuale):

        self.nome = nome
        self.priorita = priorita
        self.percentuale = percentuale

    def mostra_categoria(self):

        return (
            f"{self.nome} | "
            f"Priorità: {self.priorita} | "
            f"Percentuale: {self.percentuale}%"
        )