country = input('Enter your country ')
if country.lower() == 'canada':
    province = input('Enter your province ')
    if province.lower() in ('alberta', 'yukon', 'Nunavat'):
        tax = 5
    elif province.lower() == 'Ontario':
        tax = 13
    else:
        tax = 15
else:
    tax = 0

print('Your tax rate is  ' + str(tax))