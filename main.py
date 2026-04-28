import requests, time

print("bonjour")
url = input("entrez l'URL a tester  : ")
print("")

http_codes_accessibles = {
    # Succès
    200: "Tout fonctionne parfaitement.",
    201: "C'est fait ! Le nouvel élément a bien été créé.",
    204: "L'action a réussi, mais il n'y a rien de particulier à afficher.",

    # Problèmes de direction
    301: "Cette page a déménagé définitivement vers une nouvelle adresse.",
    302: "La page se trouve ailleurs pour l'instant.",

    # Erreurs de l'utilisateur
    400: "Il y a une erreur dans votre demande, le site ne comprend pas ce que vous voulez.",
    401: "Vous devez vous identifier (pseudo/mot de passe) pour voir ceci.",
    403: "Accès refusé : vous n'avez pas le droit d'être ici.",
    404: "Désolé, cette page n'existe pas ou a été supprimée.",
    408: "Le site a mis trop de temps à répondre, votre connexion est peut-être lente.",
    429: "Doucement ! Vous envoyez trop de demandes d'un coup, veuillez patienter.",

    # Erreurs du site (serveur)
    500: "Le site a un problème technique interne. Ce n'est pas de votre faute.",
    502: "Le site a reçu une mauvaise réponse d'un autre serveur dont il dépend.",
    503: "Le site est surchargé ou en maintenance. Revenez plus tard.",
    504: "Le site a mis trop de temps à récupérer les données. Réessayez."
}

try:
    # Correction de l'erreur de frappe : status_code au lieu de statuts_code
    requete = requests.get(url, timeout=10)
    code_a_tester = requete.status_code

    if code_a_tester in http_codes_accessibles:
        print(http_codes_accessibles[code_a_tester])
    else:
        print(f"Erreur : Le code {code_a_tester} n'existe pas dans la base.")

except requests.exceptions.RequestException:
    print("Erreur : Impossible de joindre le site (vérifiez l'URL ou votre connexion).")
    