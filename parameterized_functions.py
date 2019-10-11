def print_initials(name, force_uppercase = True):
    if force_uppercase:
        return name[0:1].upper()
    else:
        return name[0:1]

print(print_initials('sasi'))

print(print_initials(force_uppercase=False, name= 'pavi'))