class ReportService:
    
    def genera_report(
        self,
        budget
    ):
        
        print("\n========== REPORT MENSILE ==========")
        
        print(
            f"\nStipendio: "
            f"{budget.stipendio}€"
        )
        
        print(
            f"\nSaldo residuo: "
            f"{budget.saldo}€"
        )
        
        print("\n----- FONDI -----")
        
        for fondo in budget.fondi:
            
            print(
                fondo.mostra_fondo()
            )
            
        print("\n----- SPESE -----")
        
        for spesa in budget.spese:
            
            print(
                spesa.mostra_spesa()
            )
            
        print("\n========== FINE REPORT ==========")    
        
# end alternate constructor