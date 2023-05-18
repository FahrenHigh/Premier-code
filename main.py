def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom

#--------------------------------------------------------------
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Entrez un age correct.")
    return age_int

#--------------------------------------------------------------        
def afficher_informations_personne(nom, age):
    print()
    print("Vous vous appellez " + nom + " et vous avez " + str(age) + " ans.")
    print("L'an prochain vous aurez " + str(age+1) + " ans.")

    # == égal
    # < inférieur
    # <= inferieur ou égal
    # > supérieur
    # >= supérieur ou égal
    # True / False (Boolean)
    # elif -> else if
    if age == 17:
        print("Vous êtes presque majeur. ")
    elif age == 18:
        print("Tout juste majeur: Félicitation! ")
    elif age > 18:
        print("Vous êtes majeur. ")
    else:
        print("Vous êtes mineur. ")

#--------------------------------------------------------------

#Demander Nom
nom1 = demander_nom()
nom2 = demander_nom()

#Demander age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

#Résultat
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)