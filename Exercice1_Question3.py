def add (x,y):
    return x + y

def sous (x,y):
    return x - y
    
def multi (x,y):
    return x * y 

def divi (x,y):
    return x / y 

def erreur (op):
    op = input("Veuillez saisir +, -, x ou / : ")
    return op


res = 0
val1 = int(input("Entrez un premier nombre :"))
opé = input("Entrez une opération :") #Pas besoin car input chaine de cara de base
while (opé != "+" and opé != "-" and opé != "x" and opé != "/"):
    opé = erreur(opé)
val2 = int(input("Entrez un second nombre :"))

if opé == "/" and val2 == 0:
    print ("Il n'est pas possible de diviser par 0 !")
else :
    if opé == "+":
        res = add(val1, val2)
        print(val1,opé,val2, " = ", res)
    elif opé == "-":
        res = sous(val1, val2)
        print(val1,opé,val2, " = ", res)
    elif opé == "x":
        res = multi(val1,val2)
        print(val1,opé,val2, " = ", res)
    else:
        res = divi(val1,val2)
        print(val1,opé,val2, " = ", res)