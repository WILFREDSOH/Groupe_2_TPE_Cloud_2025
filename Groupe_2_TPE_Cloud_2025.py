def User_input():  # fonction qui permet à l'utilisateur d'entrée sa propre liste

    print("Entrez les éléments de ta liste, séparés par des espaces : ")
    elements = input().split()  # La méthode split() vas demander a l'utilisateur d'entrer une liste en une seule saisie et ensuite vas diviser la chaine recue en une liste d'elements distinct.
    return [int(element) for element in
            elements]  # Nous transformoons la precedente liste en liste d'entier, utiles pour identifier les doublons


def prefined_list():  # Dans le cas ou l'utilisateur ne veut saisir de liste, nous avons prédefinies des listes que l'utilisateur peut choisir

    listes = [
        [1, 2, 3, 2, 4, 5, 6, 4, 7, 8, 6],
        [10, 20, 10, 30, 40, 50, 30, "hello", "hi", "Merci"],
        [1, 1, 1, 2, 2, 3, 4, 100, 250],
        [5, 10, 15, 20, 25, 5, 30, 35, 10],
        ["Bienvenue", "Bonjour", "bonjour", "great", "good"]
    ]
    print("\nVoici des liste prédéfinit pour vous :")
    for index, liste in enumerate(
            listes):  #enumerate() est utilisée pour pouvoir parcourir la liste.
        print(f"{index + 1}. {liste}")

    choix = int(input("Choisissez une liste en entrant le numéro correspondant : ")) - 1
    return listes[choix]


print("Détection de doublons dans la liste")
print("1. Entrer votre propre liste")
print("2. Choisir une liste prédéfinie")
choix = int(input("Faites votre choix en entrant soit 1 ou 2 : "))
liste = []
if choix == 1:
    liste = User_input()
elif choix == 2:
    liste = prefined_list()
else:
    print("Choix invalide.")  # Si l'utilisateur entre un autre choix outre que 1 et 2 alors le programme affiche le message précédent
    print(f"\nListe sélectionnée : {liste}")
# Les deux boucles "for" qui suivent permettent de rearranger le tableau entre afin que les elements identiques soient cote a cote et pas necessairement triés,
# a l'aide d'une permutation 
for i in range(len(liste) - 1):
    for j in range(i + 1, len(liste)):
        if liste[i] == liste[j]:
            temp = liste[i + 1]
            liste[i + 1] = liste[j]
            liste[j] = temp
print("Les doublons de votre liste sont: ", end=' ')
k = 0
# Les boucles while ci-dessous permettent de parcourir le tableau classé de maniere à compté le nombre d'elements identiques en chaine;
# k ici est la position de depart pour chaque portion d'elements identiques, s permet de parcourir la portion jusqu'au prochain element different;
# Et enfin l permet de gerer la fin de liste et de s'assurer qu'on la parcourt entierement jusqu'au dernier element.
while k <= len(liste) - 2:
    l = k + 1
    s = k + 1
    count = 0
    while liste[k] == liste[s] and l < len(liste):
        count += 1
        s = l
        l += 1
    l = 0
    if count > 0:
        print(liste[k], end=" ")
    k = s

#On renvoi alors un par un, mais sur la meme ligne, tous les doublons de la liste. Nous n'avons pas utilisé une autre structure de données que celles que l'utilisateur a fourni.
