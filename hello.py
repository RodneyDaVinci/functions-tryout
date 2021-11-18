tafelnummer = int(input("Van welk getal wilt u de tafel zien?"))

def tafel(tafel):
    for i in range(11):
        print(tafel * i)

tafel(tafelnummer)