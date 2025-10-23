#1. samm
print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi! ")
try:
    soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
    if soov==1:
        print("Indeksi leidmine")
        # Küsi pikkust
        # Küsi massi
    elif soov==0:
        print("Kahju! See on väga kasulik info!")
    else:
        print("Vale valik. Saab valida ainult 1 või 0")
except:
    print("Vale soov!")




#2. samm
print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi! ")
try:
    soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
    if soov==1:
        print("Indeksi leidmine")
        # Küsi pikkust kuni on õiges formaadis ja vahemikus 0–250
        while True:
            try:
                pikkus = int(input("Mis on sinu pikkus (cm)? "))
                if 0 < pikkus <= 250:
                    break
                else:
                    print("Pikkus peab olema vahemikus 0 kuni 250 cm!")
            except:
                print("Vale pikkuse formaat! Palun sisesta täisarv.")
        
        
        # Küsi massi kuni on õiges formaadis ja vahemikus 0–200
        while True:
            try:
                mass = float(input("Mis on sinu kaal (kg)? "))
                if 0 < mass <= 200:
                    break
                else:
                    print("Kaal peab olema vahemikus 0 kuni 200 kg!")
            except:
                print("Vale kaalu formaat! Palun sisesta arv.")
        
        # Arvuta kehamassiindeks (KMI)
        indeks = round(mass / (0.01 * pikkus) ** 2, 2)
        print(f"{nimi}! Sinu kehamassiindeks on: {indeks}")
        # Hinda KMI. Tee seda ise
    elif soov==0:
        print("Kahju! See on väga kasulik info!")
    else:
        print("Vale valik. Saab valida ainult 1 või 0")
except:
    print("Vale soov!")