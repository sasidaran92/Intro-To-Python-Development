from array import array

scores  = array('i')
scores.append(98)
scores.append(99)
scores.append(97)

print(scores)
print(scores[0])

names = ['Sasi', 'Pavi', 'Test']
names.sort()

print(names)
print(names[1:2])

person = {'first' : 'Pavithira'}
person['last'] = 'Sasidaran'

print(person)

persons = []

persons.append(person)
print(persons)
print(len(person))
