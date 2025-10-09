paev=input("Sisesta päeva nimetus (näiteks esmaspäev): ")
#1. Kui on neljapäev, siis "Huraaa, Prgrammeerimine!
if paev.lower()=="neljapäev":
    print("Huraaa, Programmeerimine!")

#2. Kui on neljapäev, siis "Huraaa, Prgrammeerimine!, kui on reede, siis "Igatsen, prgrammeerida tahaks!".
if paev.lower()=="neljapäev":
    print("Huraaa, Programmeerimine!")
else:
    print("Igatsen, programmeerida tahaks!")
#3. Tööpaevad ja nädalavahetus
if paev.lower()=="laupäev" or paev.lower()=="pühapäev":
    print("Lõpuks ometi nädalavahetus!")
else:
    print("Tööpäev, pean tööl käima!")