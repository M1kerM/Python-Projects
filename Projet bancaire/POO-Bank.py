import random

#inputs
numero_de_compte = input("Veuillez taper votre numéro de compte : ")
nom_du_titulaire_du_compte = input("Veuillez taper le nom du titulaire du compte : ")
code_PIN =  input("Veuillez taper votre code PIN : ")
solde_du_compte = 0

#CREATION DES DIFFERENTES CLASSES

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


# 2.BANQUE
# 2.1. création de la classe Banque
class Banque:
    def __init__(self, Comptes):
        Comptes = {numero_de_compte : code_PIN, nom_du_titulaire_du_compte : solde_du_compte}

# 2.2. création des méthodes de la classe banque

# fonction pour générer aléatoirement les numéros de compte
# On génère la liste de tous les nombres à 6 chiffres puis on mélange la liste
tous_les_numéros_de_compte = list(range(100000, 1000000))
random.shuffle(tous_les_numéros_de_compte)

# Obtention du prochain numero unique
def obtention_numero_unique():
    if tous_les_numéros_de_compte:
        return tous_les_numéros_de_compte.pop()
    else:
        raise ValueError("Tous les numéros de compte ont déjà été attribués")


# 2.2.1. création de la méthode cree_compte
def cree_compte():
    nom_proprietaire_compte = input("Tapez votre nom complet : ")
    code_PIN = input("Saisissez votre code PIN(4 chiffres) : ")
    balance_initiale = 0
    numero_compte = obtention_numero_unique()
    return numero_compte, nom_proprietaire_compte, balance_initiale, code_PIN

# 2.2.2. création de la méthode get_compte
def get_compte(numero_compte):














# mon_compte = Compte(numero_de_compte, nom_du_titulaire_du_compte, code_PIN, solde_du_compte)
# print(mon_compte.numero_de_compte)
# print(mon_compte.nom_du_titulaire_du_compte)
# print(mon_compte.code_PIN)
# print(mon_compte.solde_du_compte)