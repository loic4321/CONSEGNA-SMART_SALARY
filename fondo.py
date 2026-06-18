class Fondo:

    def __init__(self, nome):

        self.nome = nome
        self.saldo = 0

    def aggiungi_importo(self, importo):

        self.saldo += importo

    def mostra_fondo(self):

        return (
            f"{self.nome} | "
            f"Saldo: {self.saldo}€"
        )