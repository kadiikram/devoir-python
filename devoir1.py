# ---------------- Programme : Gestion d’un panier de produits pour un client --------------------


# Le panier est un dictionnaire :
# - La clé : code du produit
# - La valeur : dictionnaire contenant nom, prix, quantité
panier = {}

# 1. Ajouter plusieurs produits au panier
def ajouter_produits():
    n = int(input("Combien de produits voulez-vous ajouter ? "))

    # Répéter l’opération N fois
    for _ in range(n):
        # Saisir les informations du produit
        code = input("Code du produit : ").strip()
        nom = input("Nom du produit : ").strip() 
        prix = float(input("Prix unitaire : "))
        quantite = int(input("Quantité : "))
        
        # Vérifier si le code existe déjà
        if code in panier:
            print("Ce code existe déjà ! Produit non ajouté.")
            continue  # passer au produit suivant

        # Vérifier que le prix et la quantité sont positifs
        while prix < 0:
            print("Erreur : Le prix ne peut pas être négatif. Réessayez.")
            prix = float(input("Prix unitaire : "))

        # Vérifier que la quantité est strictement positive
        while quantite <= 0:
            print("Erreur : La quantité doit être strictement positive. Réessayez.")
            quantite = int(input("Quantité : "))

        # Stocker le produit dans le panier
        panier[code] = {
            "nom": nom,
            "prix": prix,
            "quantite": quantite
        }

        print("✔ Produit ajouté avec succès !")
    print("--------------------------------------")


# 2. Calculer le total à payer
def calculer_total():
    total = 0

    # On additionne prix × quantité pour chaque produit
    for produit in panier.values():
        total += produit["prix"] * produit["quantite"]

    return total

# 3. Afficher la facture du client
def afficher_facture():
    # Vérifier si le panier est vide
    if not panier:
        print("Le panier est vide.")
        return

    print("\n============= FACTURE =============")
    print("Code     Nom          Quantité   Prix U.")
    print("----------------------------------------")

    # Trier les produits selon le code (ordre alphabétique)
    for code in sorted(panier.keys()):
        p = panier[code]
        print(f"{code}     {p['nom']}        {p['quantite']}         {p['prix']}")

    print("Prix total :", calculer_total(), "DH")

# 4. Modifier un produit
def modifier_produit():
    code = input("Entrez le code du produit à modifier : ")

    # Vérifier si le produit existe
    if code not in panier:
        print("Produit introuvable.")
        return

    print("Que voulez-vous modifier : ")
    print("1. Code")
    print("2. Nom")
    print("3. Prix")
    print("4. Quantité")

    choix = input("Votre choix : ")

    # Modifier le code
    if choix == "1":
        nouveau_code = input("Nouveau code : ")
        panier[nouveau_code] = panier.pop(code)
        print("Code modifié !")

    # Modifier le nom
    elif choix == "2":
        panier[code]["nom"] = input("Nouveau nom : ")
        print("Nom modifié !")

    # Modifier le prix
    elif choix == "3":
        panier[code]["prix"] = float(input("Nouveau prix : "))
        print("Prix modifié !")

    # Modifier la quantité
    elif choix == "4":
        panier[code]["quantite"] = int(input("Nouvelle quantité : "))
        print("Quantité modifiée !")
    else:
        print("Choix invalide.")

# 5. Supprimer un produit
def supprimer_produit():
    code = input("Entrez le code du produit à supprimer : ")
    removed = panier.pop(code, None)
    
    if removed:
      print("Produit supprimé !")
    else:
      print("Produit introuvable.")

# Menu principal du programme
def menu():
    while True:
        print("\n--------------- MENU ----------------")
        print("1. Ajouter les produits")
        print("2. Calculer le prix total")
        print("3. Afficher la facture totale")
        print("4. Modifier un produit")
        print("5. Supprimer un produit")
        print("0. Quitter")
        print("--------------------------------------")

        choix = input("Votre choix : ")

        match choix:
            case "1": ajouter_produits()
            case "2": print("Prix total :", calculer_total(), "DH")
            case "3": afficher_facture()
            case "4": modifier_produit()
            case "5": supprimer_produit()
            case "0": 
                print("Au revoir !")
                break
            case _: print(" Choix invalide, réessayez.")