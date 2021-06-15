#christopher robin kaasik
#it20
#Seiklus mäng milles sa pead põgenema koletise eest
from pathlib import Path
import random
import json
#küsib kas tahad mängida
answer = input("alustame mänguga ? (y/n): ")
karakter = input("Sisestage enda nimi: ")
#kontrollib kasutaja olemasolu
if Path(karakter+".txt").is_file():
    print(karakter+" on juba olemas")
    print("tervist, " + karakter)
    f = open(karakter+".txt").read()
    ATK = int(eval()["ATK"])
    DEF = int(eval()["DEF"])
    print("ATK:", (ATK))
    print("DEF:", (DEF))
else:
    print("teekond algab siit.")

    Nimi = karakter
    ATK = 10
    DEF = 10
    print("praegused andmed:\nATK: ", ATK, "\nDEF: ", DEF)
    k = (str(input("valida on (ATK(1)/DEF(2)), kumba lisad oma punktid? : ")))
    #punktide lisamine
    if k == "1":
        ATK = ATK + 10
        print("ATK: 20")
        print("DEF: 10")
    elif k == "2":
        ATK = 10
        DEF = DEF + 10
        print("ATK: 10")
        print("DEF: 20")
        print("karakter "+karakter+" on nüüd olemas")
        punktid = {
            "Nimi": Nimi,
            "ATK": ATK,
            "DEF": DEF
        }
        #lisab andmed txt faili
        with open(karakter+'.txt', 'w') as convert_file:
         convert_file.write(json.dumps(punktid))
    if answer.lower().strip() == "y":
    
        answer = input ("saabud ristteele, tahad minna '1'(paremale) või '2' (vasakule)?: ")
        if answer == "2":
            answer = input("saabus su ette koletis, tahad '3'(jookse) või '4'(võitle)?: ")
            
            if answer == "4":
                print("koletis oli sinu jaoks liiga tugev, kaotasid!")
            else:
                print("hea mõte, pääsesid puhta nahaga!")
                
                answer = input(f"kõnnid kaua, on pime näed kaugel tulesid, see tähendab et seal asub linn kus saaks puhata. Kas tahad minna või püsida koha peal? (mine/püsi): ")
                
            if answer == "mine":
                print("lähened linnale...")
                print("Sa kõndisid terve päev ")
            else:
                print("sa jäid ööseks välja, külmusid surnuks. Mäng Läbi")
                         
        elif answer == "1":
            print("sa oled väsinud, sul on külm ja silmad on vaevu lahti aga sa ei taha alla anda, sa kõnnid ja kõnnid kuni tuleb kari hunte põõsastest välja ja söövad su ära. Mäng läbi")
            
def voitlus():            
    mhealth = 10
    ehealth = 10
    lives = 1
    #combat
    while (ehealth>=0 and mhealth>=0) or lives==1:
        ehit = random.randint(1,10)
        if ehit==1:
            ehealth = ehealth-random.randint(5,10)
            
            mhit = random.randint(1,3)
            if mhit==1:
                mhealth = mhealth-random.randint(5,10)
            print(f"elud: {ehealth}")
            print(f"elud: {mhealth}")
            if mhealth>ehealth:
                print("Võit!!")
                ehealth = 5
                mhealth = 5
            else:
                print("kaotus")
                lives = 0
        k()