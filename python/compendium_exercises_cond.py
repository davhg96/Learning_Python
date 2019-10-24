print('Conditionals \n Exercise 1 \n')#################

name=input('Please identify yourself: ')

if name.lower()=='david':
    print('Hello there mi lord')
else:
    print('Hello there stranger')

print('\n Exercise 2 \n')#############################

name=input('Please identify yourself: ')
friens=['nino', 'maroulitsa', 'maria','malou', 'joel']
if name.lower()=='david':
    print('Hello there mi lord')
elif name.lower() in friens:
    print('Hello there friend')
else:
    print('Hello there stranger')


print('\n Exercise 3 \n')############################

number=int(input('Insert number (digit): '))
if number%3==0 and number%5==0:
    print('FizzBuzz')
elif number%5==0:
    print('Buzz')
elif number%3==0:
    print('Fizz')
else:
    print(number)

print('\n Exercise 4 \n')############################

for n in range(1,101):
  if n%3==0 and n%5==0:
      print(n,'\n''FizzBuzz')
  elif n%5==0:
      print(n,'\n''Buzz')
  elif n%3==0:
      print(n,'\n''Fizz')
  else:
      print(n)
