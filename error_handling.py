num1 = input('Enter number 1 ')
num2 = input('Enter number 2 ')

try:
    print('Dividing numbers')
    print(float(num1)/float(num2))
except ZeroDivisionError as e:
    print('Division Failed')
except:
    print('Unknown error')
finally:
    print('Exiting')