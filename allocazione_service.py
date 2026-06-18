from models.fondo import Fondo


class AllocazioneService:

    def alloca_budget(
        self,
        budget
    ):

        for categoria in budget.categorie:

            quota = (
                budget.stipendio
                * categoria.percentuale
            ) / 100

            fondo = Fondo(
                categoria.nome
            )

            fondo.aggiungi_importo(
                quota
            )

            budget.aggiungi_fondo(
                fondo
            )