import datetime

def print_time(text):
    print(text)
    print(datetime.datetime.now())
    print()

print_time('Task Started')
for index in range(0,9):
    print(index)
print_time('Task Completed')

def print_intials(firstname, lastname):
    return (firstname[0:1].upper() + lastname[0:1].upper())

firstname = input('Enter your Firstname: ')
lastname = input('Enter your Lastname: ')

print(print_intials(firstname, lastname))