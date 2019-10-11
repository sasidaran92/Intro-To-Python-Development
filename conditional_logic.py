price = input('Enter the price of the food item ')

if float(price) >= 1.00:
    tax = 0.37
else:
    tax = 0
print('Your tax ' + str(tax))