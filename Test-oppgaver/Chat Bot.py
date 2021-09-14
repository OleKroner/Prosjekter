from time import sleep

on = True
turn = 0

while on:
    
    if turn == 0:
        info = input("\n\033[1;36;40mHva vil du vite om meg?:\n\n\033[0;37;40m   1 - Hva heter jeg?\n   2 - Hvor gammel er jeg?\n   3 - Hva er mine interesser?\n   4 - Hvilke teknologier har jeg brukt?\n\n   0 - Avslutt\n\n\033[1;36;40mSvar:  \033[0;37;40m")
    
    else:
        sleep(3)
        info = input("\n\033[1;36;40mAlternativer:\n\033[0;37;40m   1 - Hva heter jeg?\n   2 - Hvor gammel er jeg?\n   3 - Hva er mine interesser?\n   4 - Hvilke teknologier har jeg brukt?\n\n   0 - Avslutt\n\n\033[1;36;40mEr det noe mer du vil vite om meg?:   \033[0;37;40m")
    
    try:
        info = int(info)
    
    except ValueError:
        print("\033[1;31;40m\nDu må skrive inn et tall!\033[0;37;40m")
        sleep(2)
    
    else:
        if info == 1:
            turn =1
            print("\n\033[0;32;40m   Jeg heter Ole Kristoffer Trandem.\033[0;37;40m")

        elif info == 2:
            turn = 1
            print("\n\033[0;32;40m   Jeg er 17 år og har bursdag den 2 april.\033[0;37;40m")
            
        elif info == 3:
            turn = 1
            print("\n\033[0;32;40m   Jeg bruker mesteparten av fritiden min på spilling,\n   men liker også å holde på med noen hobby prosjekter innenfor programmering og teknologi.\033[0;37;40m")
            
        elif info == 4:
            turn = 1
            print("\n\033[0;32;40m   Innenfor programmering er Python og PHP de programmeringsspråkene jeg kjenner til best.\n   Det største prosjektet jeg har jobbet på er å lage en utlånsdatabase for utlån av utstyr.\n   Der brukte jeg HTML, CSS, PHP og MySQL til å lage systemet.\n   I python har jeg lagd mer småprogrammer og spill, som tic-tac-toe med en bot og sjakk med et library kalt PyGame.\n   Utenom det har jeg ganske god forståelse innenfor alt om nettverk, internett og PC-er.\033[0;37;40m")
        
        elif info == 0:
            on = False
            
        else:
            print("\033[1;31;40m\nDu må velge et av alternativene over!\033[0;37;40m")
            sleep(3)
