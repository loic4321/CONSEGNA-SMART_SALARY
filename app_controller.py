from models.budget import BudgetMensile
from models.categoria import Categoria
from models.spesa import Spesa

from services.allocazione_service import AllocazioneService
from services.report_service import ReportService

from repositories.budget_repository import BudgetRepository

from models.utente import Utente


from services.budget_service import BudgetService

class AppController:

    def start(self):

       
        nome = input(
            "Inserisci il tuo nome: "
       )
       
        email = input(
            "Inserisci la tua email: "
        )
        
        utente = Utente(
            nome,
            email
        )
        
        while True:
            
            stipendio = float(
                input(
                    "Inserisci il tuo stipendio: "
                )
            )
            
            if stipendio > 0:
                
                break
            
            print(
                "Lo stipendio deve essere maggiore di zero. Riprova."
            )
       
        budget_service = BudgetService()
        
        budget = budget_service.crea_budget(
            stipendio
        )
        
        utente.assegna_budget(
            budget
        )
        

        repository = BudgetRepository()

        repository.salva_budget(
            budget
        )

        print(
            "\nBudget salvato correttamente."
        )

        categoria1 = Categoria(
            "Spese Fisse",
            1,
            50
        )

        categoria2 = Categoria(
            "Imprevisti",
            2,
            20
        )

        categoria3 = Categoria(
            "Piacere",
            3,
            10
        )

        categoria4 = Categoria(
            "Risparmio",
            1,
            20
        )

        budget_service.aggiungi_categoria(
            budget,
            categoria1
        )
        

        budget_service.aggiungi_categoria(
            budget,
            categoria2
        )

        budget_service.aggiungi_categoria(
            budget,
            categoria3
        )

        budget_service.aggiungi_categoria(
            budget,
            categoria4
        )

        allocazione = AllocazioneService()

        allocazione.alloca_budget(
            budget
        )

        print("\nRegistrazione spese")

        while True:
            
            print("\nRegistrazione spese")
            
            nome_spesa = input(
                "Nome della spesa: "
            )
            
            while True:
                
                importo_spesa = float(
                    input(
                        "Importo della spesa: "
                    )
                )
                
                if importo_spesa > 0:
                    
                    break
                
                print(
                    "L'importo della spesa deve essere maggiore di zero. Riprova."
                )
            
            print("\nScegli la categoria:")
            
            print("1 - Spese Fisse")
            print("2 - Imprevisti")
            print("3 - Piacere")
            print("4 - Risparmio")
            
            scelta = int(
                input(
                    "Categoria: "
                )
            ) 
            
            if scelta == 1:
                
                categoria_scelta = categoria1
                
            elif scelta == 2:
               
                categoria_scelta = categoria2
                
            elif scelta == 3:
                
                categoria_scelta = categoria3
            
            elif scelta == 4:
                
                categoria = categoria4
            
            else:
                
                print("Categoria non valida.")
                
                continue

            spesa = Spesa(
                nome_spesa,
                importo_spesa,
                categoria_scelta
            )
            
            budget_service.aggiungi_spesa(
                budget,
                spesa
            )
            
            altra_spesa = input(
                "Vuoi inserire un'altra spesa? (s/n): "
            )
            
            if altra_spesa.lower() != "s":
                
                break

        print("\n--- BUDGET ---")

        print(
            budget.mostra_budget()
        )

        print("\n--- FONDI ---")

        for fondo in budget.fondi:

            print(
                fondo.mostra_fondo()
            )

        report = ReportService()

        report.genera_report(
            budget
        )