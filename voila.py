class Voiture:
    def __init__(self, marque, modele, vitesse, moteur):
        self.marque= marque
        self.modele= modele
        self.vitesse= vitesse
        self.moteur= moteur

    def accelerer(self):
        self.vitesse+= 10

    def afficher_vitesse(self):
        print(self.vitesse)



voiture1= Voiture("Renault", "206", 30, "diesel")
voiture1.accelerer()
voiture1.afficher_vitesse()