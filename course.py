def gestionnaire_courses():
    liste_courses = []

    while True:
        print("\n1. Ajouter un article")
        print("2. Supprimer un article")
        print("3. Afficher la liste de courses")
        print("4. Quitter")
        choix = input("Choisis une option: ")

        if choix == '1':
            article = input("Entrez le nom de l'article à ajouter: ")
            liste_courses.append(article)
        elif choix == '2':
            article = input("Entrez le nom de l'article à supprimer: ")
            if article in liste_courses:
                liste_courses.remove(article)
                print(f"L'article '{article}' a été supprimé.")
            else:
                print(f"L'article '{article}' n'est pas dans la liste.")
        elif choix == '3':
            print("Liste de courses:")
            for idx, article in enumerate(liste_courses, start=1):
                print(f"{idx}. {article}")
        elif choix == '4':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

gestionnaire_courses()
