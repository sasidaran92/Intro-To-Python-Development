from array import array

scores  = array('i')
scores.append(98)
scores.append(99)
scores.append(97)

for index in range(1,2):
    print(scores[index])

index = 0
while index < len(scores):
    print(scores[index])
    index = index + 1

names = ['Sasi', 'Pavi', 'Test']
for name in names:
    print(name)
