name = str(input('Name: '))
while True:
    try:
        math_grade = float(input('Math Grade: '))
        break
    except ValueError:
        print('Invalid Input')
        continue
while True:
    try:
        science_grade = float(input('Science Grade: '))
        break
    except ValueError:
        print('Invalid Input')
        continue
while True:
    try:
        english_grade = int(input('English Grade: '))
        break
    except ValueError:
        print('Invalid Input')
        continue

ave = (math_grade + science_grade + english_grade) / 3

if ave >= 75:
    status = 'PASSED'
elif ave < 75:
    status = 'FAILED'
else:
    status = 'Invalid'

print('Name:', name)
print('Math Grade:', math_grade)
print('Science Grade:', science_grade)
print('English Grade:', english_grade)
print('Average: %0.2f' % ave)
print('Status:', status)

