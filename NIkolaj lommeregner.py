navnet = input('skriv dit navn: ')
print('hej', navnet)
valg = input('vil du gange eller pluds')

def gange():
    try:
        etTal = int(input('Giv mig et tal: '))
    except:
        print("det virkede ikke")

    etAndetTal = int(input('Giv mig et andet tal: '))

    summen = etTal*etAndetTal
    print('Summen af de to tal er: ', summen, ',', navnet, '.. Vidste du ikke det?')

    print()


if valg == '*':
    gange()


def pluds():
    try:
        etTal = int(input('Giv mig et tal: '))
    except:
        print("det virkede ikke")

    etAndetTal = int(input('Giv mig et andet tal: '))

    summen = etTal + etAndetTal
    print('Summen af de to tal er: ', summen, ',', navnet, '.. Vidste du ikke det?')

    print()

if valg == '+':
    pluds()
