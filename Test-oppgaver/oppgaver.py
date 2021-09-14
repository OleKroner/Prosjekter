import random
from time import sleep

def oppg1():
    frukt = "agurk"
    grønnsak = "eple"
    print(frukt + " er en frukt og " + grønnsak +  " er en grønnsak")
    frukt, grønnsak = grønnsak, frukt
    #grønnsak = "agurk"
    print(frukt + " er en frukt og " + grønnsak +  " er en grønnsak")


def oppg2():

    tall1 = 14
    tall2 = 7
    tall3 = 11

    if tall1 > tall2 and tall1 > tall3:

        print(str(tall1) + " er større enn " + str(tall2) + " og " + str(tall3))
 
    elif tall2 > tall1 and tall2 > tall3:

        print(str(tall2) + " er større enn " + str(tall1) + " og " + str(tall3))

    else:

        print(str(tall3) + " er større enn " + str(tall2) + " og " + str(tall1))


def oppg3():

    navnEn = "Jonatan"
    navnTo = "Tobias"

    if len(navnEn) > len(navnTo):
        print(navnEn + " (" + str(len(navnEn)) + " bokstaver) har lengre navn enn " + navnTo + " (" + str(len(navnTo)) +" bokstaver)")
    
    elif len(navnEn) < len(navnTo):
        print(navnTo + " (" + str(len(navnTo)) + " bokstaver) har lengre navn enn " + navnEn + " (" + str(len(navnEn)) +" bokstaver)")
    
    else:
        print(navnEn + " (" + str(len(navnEn)) + " bokstaver) har like langt navn som " + navnTo + " (" + str(len(navnTo)) +" bokstaver)")


def oppg4(oppgDel):

    start = 1
    slutt = 12

    if oppgDel == 1:
        
        for i in range(start, slutt, 1):
            print(i)

    else:

        for i in range(slutt, start, -1):
            print(i)   


def oppg5():

    tilfeldigTall = 0

    while tilfeldigTall != 571:

        tilfeldigTall = random.randint(1, 999)
        print(tilfeldigTall)
        if tilfeldigTall == 571:
            print("Ferdig!")


def oppg6(oppgDel):

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []

    print(a)

    if oppgDel == 1:

        for number in a:
            print(number)

    elif oppgDel == 2:

        for number in a:
            if number < 5:
                print(str(number) + " er mindre enn 5")
    
    elif oppgDel == 3:
            
        for number in a:
            if number % 2 == 0:
                print(str(number) + " er et partall")
    
    elif oppgDel == 4:

        for number in a:
            if number > 5:
                b.append(number)

        print(b)            

    
def oppg7():

    høyde = input("\nHvor høy er du?: ")
    vekt = input("Hvor mye veier du?: ")

    try:

        int(høyde)
        int(vekt)

    except ValueError:

        print("\nBegge verdiene må være et tall!")
        sleep(2)
        oppg7()
    
    else:

        høyde = int(høyde)
        vekt = int(vekt)

        bmi_IkkeAvrundet = vekt / ((høyde/100) * (høyde/100))
        bmi = float("{:.1f}".format(bmi_IkkeAvrundet))

        
        if bmi <= 16:
            print("\nDu har en BMI på " + str(bmi) + " og er undervektig grad 3")
        
        elif bmi <= 17:
            print("\nDu har en BMI på " + str(bmi) + " og er undervektig grad 2")

        elif bmi <= 18.5:
            print("\nDu har en BMI på " + str(bmi) + " og er undervektig grad 1")
        
        elif 25 > bmi > 18.5:
            print("\nDu har en BMI på " + str(bmi) + " og har en normal vekt")
        
        elif 30 > bmi > 25:
            print("\nDu har en BMI på " + str(bmi) + " og er overvektig")
        
        elif 35 > bmi > 30:
            print("\nDu har en BMI på " + str(bmi) + " og har fedme")
        
        elif 40 > bmi > 35:
            print("\nDu har en BMI på " + str(bmi) + " og har alvorlig fedme")

        elif bmi > 40:
            print("\nDu har en BMI på " + str(bmi) + " og har svært alvorlig fedme")

def main():
    
    print("\nHvilke oppagave vil du se?")
    print("\n   1 - Oppgave 1")
    print("   2 - Oppgave 2")
    print("   3 - Oppgave 3")
    print("   4a - Oppgave 4a")
    print("   4b - Oppgave 4b")
    print("   5 - Oppgave 5")
    print("   6a - Oppgave 6a")
    print("   6b - Oppgave 6b")
    print("   6c - Oppgave 6c")
    print("   6d - Oppgave 6d")
    print("   7 - Oppgave 7")

    svar = input("\nSvar: ")

    if svar == "1":
        oppg1()
    
    elif svar == "2":
        oppg2()
    
    elif svar == "3":
        oppg3() 

    elif svar == "4a":
        oppg4(1)
    
    elif svar == "4b":
        oppg4(1)
    
    elif svar == "5":
        oppg5()
    
    elif svar == "6a":
        oppg6(1)
    
    elif svar == "6b":
        oppg6(2)
    
    elif svar == "6c":
        oppg6(3)
    
    elif svar == "6d":
        oppg6(4)
    
    elif svar == "7":
        oppg7()
    
    else:
        print("\nVelg et av alternativene over!")
        sleep(2)
        main()



if __name__ == "__main__":
    main()