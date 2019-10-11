from datetime import datetime, timedelta

current_date = datetime.now()
print('Time now: ' + str(current_date))

yesterday = timedelta(days=1)
print('yesterday ' + str(current_date - yesterday))

print(current_date.day)

birthday = input('When is your Birthday? ')
birth_date  = datetime.strptime(birthday , '%d/%m/%Y')
print('Birthday '+ str(birth_date))