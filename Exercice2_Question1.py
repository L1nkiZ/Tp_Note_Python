def prochaine_ligne(prec):
    cour = []
    res = prec
    for i in range (len(prec)):
        if i == 0:
            cour = [1]
            prec = cour 
        else:
            cour[i] = prec[i - 1] + prec[i]
        if res == cour:
            return cour[i+1]



print(prochaine_ligne([1, 3, 3, 1]))
