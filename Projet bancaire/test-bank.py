
# 1.COMPTE
#création de la classe Compte
class Compte :
    def __init__(self, numero_de_compte, nom_du_titulaire_du_compte, solde_du_compte, code_PIN):
        self.numero_de_compte = numero_de_compte
        self.nom_du_titulaire_du_compte = nom_du_titulaire_du_compte
        self.code_PIN = code_PIN
        self.solde_du_compte = solde_du_compte

    #création des méthodes de la classe Compte

    #méthode dépôt
    def dépôt(self):
        montant_du_dépôt = int(input("Tapez le montant à déposer : "))
        self.solde_du_compte = self.solde_du_compte + montant_du_dépôt
        print(f'Vous avez déposé {montant_du_dépôt}$. Votre nouveau solde est de {self.solde_du_compte}$')
        return self.solde_du_compte

    #méthode retrait
    def retrait(self):
        code_PIN = input("Tapez votre code PIN : ")
        while code_PIN != self.code_PIN:
            print("Mot de passe incorrect")
            break
        else:
            montant_du_retrait = int(input("Tapez le montant à retirer : "))
            if montant_du_retrait > self.solde_du_compte:
                print(f'Solde insuffisant. Votre solde actuel est de {self.solde_du_compte}$')
            else :
                self.solde_du_compte -= montant_du_retrait
                print(f'Vous avez retiré {montant_du_retrait}$. Votre nouveau solde est {self.solde_du_compte}$.')
        return self.solde_du_compte

    #méthode pour obtenir la balance
    def get_balance(self):
        print(f'Votre solde est de {self.solde_du_compte}$')

    #méthode __str__()
    def __str__(self):
        print(f"Compte {self.numero_de_compte} - Titulaire : {self.nom_du_titulaire_du_compte} - Solde : {self.solde_du_compte}$")

# Interface Utilisateur

def main():
    print("Bienvenue dans notre interface utilisateur. Veuillez créer un compte.")
    numero_de_compte = input("Votre numéro de compte : ")
    nom_du_titulaire_du_compte = input("Nom du titulaire de compte : ")
    code_PIN = input("Votre code PIN : ")
    solde_du_compte = 0
    nouveau_compte = Compte(numero_de_compte, nom_du_titulaire_du_compte, solde_du_compte, code_PIN)

    while True:
        print("\nVeuillez choisir une opération : ")
        print("1. Dépôt")
        print("2. Retrait")
        print("3. Obtenir le solde")
        print("4. Obtenir les informations du compte")
        print("5. Quitter")
        opération = input("Tapez le chiffre correspondant à votre choix : ")
        
        if opération == "1":
            nouveau_compte.dépôt()
        elif opération == "2":
            nouveau_compte.retrait()
        elif opération == "3":
            nouveau_compte.get_balance()
        elif opération == "4":
            nouveau_compte.__str__()
        elif opération == "5":
            print("Merci d'avoir utilisé notre interface")
            break
        else :
            print("Opération invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()