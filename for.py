import random

def terningkast():

    terning1 = 0
    terning2 = 0
    kast = 0

    while terning1 + terning2 != 12:
        
        kast += 1
        terning1 = random.randint(1,6)
        terning2 = random.randint(1,6)
        print(terning1 + terning2)
        if terning1 + terning2 == 12:
            print("Det tokk " + str(kast) + " kast for å få 2 seksere!")

def forloop():

    for i in range(71):
        print(i)
        if 70/2==i:
            print("Du er halvveis!")
        
        if i % 7 == 0:
            print("tallet er delelig med 7!")


def liste():

    elever = []
    svar = ""

    while svar != "stop":

        svar = input("Navn på elev: ")

        if svar != "stop":
            elever.append(svar)
        
        else:
            for x in elever:
                print(x)   

liste()
