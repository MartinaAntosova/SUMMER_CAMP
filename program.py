# Vypiš čísla od 1 do 100 (včetně). Pokud je číslo dělitelné 3, vypiš "Crackle" místo čísla. Pokud je dělitelné 5, vypiš "Pop". 
# Jestli je dělitelné 3 a 5, vypiš "CracklePop".
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("CracklePop")    
    elif number % 3 == 0:
        print("Crackle")
    elif number % 5 == 0:
        print("Pop")
    else:
        print(number)
