def nL(naam:str, leeftijd:int):
    print(f'Jou naam is {naam} en je leeftijd is {leeftijd} jaar.')
while True:
    naam = input('Geef uw naam op: ')
    leeftijd = int(input('Geef uw leeftijd op: '))
    nL(naam, leeftijd)
    if input('Wilt u nog een keer naam en leeftijd opgeven? Typ stop als u wilt stoppen: ') == 'stop':
        break

nL()