amountD = (input("One item costs dollars:"))
amountC = (input("and cents: "))
amount = float(amountD+"."+amountC)
quantity = int(input("Customer bought "))

totalAm = float(amount * quantity)

print("Total is ", totalAm, "$")
