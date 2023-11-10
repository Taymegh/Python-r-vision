class compteBancaire:
    def __init__(self, montant_initial):
        self.montant_initial= montant_initial
    
    def deposer(self, montant):
        self.montant_initial+= montant
        print(f"Vous avez déposé {montant}. Votre solde est maintenant de {self.montant_initial} euros.")
    
    def retirer(self, montant):
        if self.montant_initial<montant:
            print(f"Vous avez demandé {montant} euros mais vous possédez seulement {self.montant_initial} euros sur votre compte.")
        elif self.montant_initial> montant:
            self.montant_initial-= montant
            print(f"Vous avez retiré {montant} euros. Votre solde est maintenant de {self.montant_initial} euros.")


compte1= compteBancaire(200)
compte1.deposer(300)
# print(compte1.montant_initial)
print("")
compte2 = compteBancaire(150)
compte2.retirer(300)
