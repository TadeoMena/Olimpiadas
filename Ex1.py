import math
def zetadieta(C,P,G):
    Ccant = math.ceil(C/27)
    Ccal = Ccant*105
    Pcant = math.ceil(P/30)
    Pcal = Pcant*120
    Gcal = G*9
    CalTotal = Ccal+Pcal+Gcal
    return str(CalTotal)
def verif(val):
    while val.isnumeric() == True:
        val = int(val)
        if val < 0 or val > 10**9:
            val = input("El valor debe estar entre 0 y 10 elevado a 9 ")
        else:
            return val
    else:
        exit("El valor debe ser un número, terminando programa...")
Carb = verif(input("Ingrese la cantidad de carbohidratos que desea incluir en su dieta "))
Prot = verif(input("Ingrese la cantidad de proteinas que desea incluir en su dieta "))
Gra = verif(input("Ingrese la cantidad de grasas que desea incluir en su dieta "))

print("La cantidad total de calorias será de " + zetadieta(Carb,Prot,Gra))