print('Chapter 1 \n compendium questions \n arithmetics')

import math
print('exercise 2')
print(round(int(4.6)))
print(int(round(4.6)))

print('exercise 3')
print (int(-3.1))
print(math.floor(-3.1))
print(math.ceil(3.1))

print('Chapter 1 \n compendium questions \n STRINGS')

print('exercise 2')
print('I guess its 1')
print(len(str(len('len'))))

print('exercise 3 \n A)')
my_stringA="ATCG"
my_stringA=(my_stringA+'XXX')
print(my_stringA)
print('\n')
print('B)')
my_stringB='ATGC'
n=0
while n<3:
  my_stringB=(my_stringB+'ATGC')
  n+=1
  print(my_stringB)
print('another way')
my_stringB='ATGC'
print(my_stringB*4)
print('\n')
print('C)')
print(len(my_stringB))
print('\n')
print('D)')
chain='AAAAGGAAAAGGAAAA'
print(chain.find('GG'))
#for all the GG
positions=chain.find('GG'),chain[chain.find('GG')+1: ].find('GG')+chain.find('GG')+1
print(positions)
print('\n')
print('E)')
print(chain.count('AAA'))
print(chain.count('AA'))
print(chain.count('A'))
print('\n')
print('F)')
str1='AcgT'
str2='acGT'
condition=str1.upper()==str2.upper()
print(condition)
if condition==True:
  print('Same sequence')
else:
  print('Not the same sequence')


print('\n')
print('Exercise 4')

name='Karl'
surname='Johanson'
print('My name is '+ name + ' '+ surname)
print('My name is '+ '{} {}'.format(surname, name))
print('My name is '+ '{1}{1}'.format(surname, name))
print('My name is '+ '{1}{1} {0:.5}'.format(surname, name))
print('My name is '+ '{1}{1} {0:>10.5}'.format(surname, name))
