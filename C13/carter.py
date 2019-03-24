#1
def printName():
    print("  CCCC         A        RRRRR    TTTTTTT  EEEEEEE  RRRRR")
    print(" C    C       A A       R    R      T     E        R    R")
    print("C            A   A      R    R      T     EEEEEEE  R    R")
    print("C           AAAAAAA     RRRRR       T     E        RRRRR")
    print(" C    C    A       A    R    R      T     E        R    R")
    print("  CCCC    A         A   R     R     T     EEEEEEE  R     R")


# #2
# def info(name, address, street, city, states, post_code):
#     print(name)
#     print(address)
#     print(street)
#     print(city)
#     print(states)
#     print(post_code)
#
#
# info("cici", "xiaoying", "anningzhuang", "beijing", "haidian", "10085")
#
#
# #3
# def calculateTax(price,tax_rate):
#     total = price + (price * tax_rate)
#     global  my_price
#     print("my_price (inside function =)",my_price)
#     return total
#
# my_price = float(input ("Enter a price:"))
#
# totalPrice = calculateTax(my_price, 0.06)
# print ("price = ",my_price, "totalPrice=",totalPrice)
# print("my_price (outside function =)",my_price)
#
# #4

def sum(quarters, dimes, nickels, pennies):
    print("quarters:",quarters)
    print("dimes:",dimes)
    print("nickels:",nickels)
    print("pennies:",pennies)
    print("total is $",round(0.25*quarters+0.1*dimes+0.05*nickels+0.01*pennies,2))

# printName()
# sum(3,6,7,2)