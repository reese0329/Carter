def calculateTax(price,tax_rate):
    total = price + (price * tax_rate)
    return total

my_price = float(input ("Enter a price:"))

totalPrice = calculateTax(my_price, 0.06)
print ("price = ",my_price, "totalPrice=",totalPrice)