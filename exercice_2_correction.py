def prochaine_ligne(prec):
    cour = [1]

    # Remarque : len(prec) == len(cour) - 1 à la fin de la procédure
    for i in range(1, len(prec)):
        cour.append(prec[i-1] + prec[i])

    if len(prec) > 0:  # Cas particulier
        cour.append(1)

    return cour


# print("prochaine_linge([]) =", prochaine_ligne([]))
# print("prochaine_ligne([1, 3, 3, 1]) =", prochaine_ligne([1, 3, 3, 1]))


def triange_de_pascal(rang_max):
    ligne = []

    for i in range(rang_max+1):
        ligne = prochaine_ligne(ligne)
        print("rang", i, "= ", end='')
        for e in ligne:
            print(e, end=' ')
        print()


rang_max = int(input("N ? "))
triange_de_pascal(rang_max)
