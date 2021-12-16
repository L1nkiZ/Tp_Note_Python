def rang(n):
    cour = []
    val = int(input("Entrez la taille du triangle :"))
    while (val < 0):
        val = int(input("Entrez un nombre suppérieur à 0 :"))
    for i in range (n):
        cour = cour[i] + [prochaine_ligne(cour)]
    return cour


print(rang(6))
