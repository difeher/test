from cs50 import get_int
from cs50 import get_string
from cs50 import get_float

def main():
    c=get_change()

    initialcents = (c*100)
    #print(initialcents)

    quarters = get_quarters(initialcents)
    cents = initialcents - quarters *25
    #print(f"there are {cents} cents left with {quarters} quarters used ")

    dimes = get_dimes(cents)
    cents = cents - dimes *10
    #print(f"there are {cents} cents left with {quarters} quarters and {dimes} dimes used ")

    nickels = get_nickels(cents)
    cents = cents - nickels *5
    #print(f"there are {cents} cents left with {quarters} quarters, {dimes} dimes and {nickels} nickels used ")

    pennies = get_pennies(cents)
    cents = cents - pennies *1
    #print(f"there are {cents} cents left with {quarters} quarters, {dimes} dimes, {nickels} nickels used and {pennies} pennies.")

    total_coins=quarters+dimes+nickels+pennies
    print(total_coins)
def get_change():
    while True:
        change = get_float("Cash owed:")
        if 0<change:
            break
    return change

def get_quarters(cents):
    coins = 0
    while cents>=coins*25:
        coins = coins+1
    quarters = coins-1
    return quarters
def get_dimes(cents):
    coins = 0
    while cents>=coins*10:
        coins = coins+1
    dimes = coins-1
    return dimes
def get_nickels(cents):
    coins = 0
    while cents>=coins*5:
        coins = coins+1
    nickels = coins-1
    return nickels
def get_pennies(cents):
    coins = 0
    while cents>=coins*1:
        coins = coins+1
    pennies = coins-1
    return pennies

main()
