# hier word de berekening gedaan

def fibonacci(n):
    if n < 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

# hier kan de gebruiker de aantal van de reeks opgeven die de gebruiker wilt zien

reeks = int(input('Hoeveelheid aantal wilt u zien?: '))

# hier bekijkt de code of het aantal wel geldig is

if reeks <= 0:
    print('Vul een geldige hoeveelheid in: ')
else:
  
# hier word de reeks naar de output geprint  
    print("Fibonacci reeks:")
    for i in range(reeks):
        print(fibonacci(i))