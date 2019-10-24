0#List management
numbers=[7,10,4,2]
new_numbers=numbers[1:3]# will take 10 and 4 because the third one is exclusive
new_numbers=numbers[1:] # wil take from 0 to the end
new_numbers=numbers[:]# will copy

numbers=[1,2,3,4,5,6,7,8,9,10]
evens=numbers[1::2]# will take from the 2 to the end every second number
odd=numbers[0::2]# will take from the 1 to the end every second number
odd=numbers[0::3]# will take from the 1 to the end every third number
last=numbers[-1] # this gets the last (10)
last=numbers[-1] # this gets the second last (9)
reverse=numbers[::-1]# take the wole list cointing from the end AKA reverse it
reverse=numbers[::-2]# take the wole list from the end every second




##pass
for i in range(2,10):
    if i%2==0:
        print('found an even number',i)
        pass #will stop there
    print('found an odd number', i)


##continue
for i in range(2,10):
    if i%2==0:
        print('found an even number',i)
        continue
    print('found an odd number', i)

## compare
for i in range(2,10):
    if i%2==0:
        print('found an even number',i)
        continue
        print('found an odd number', i) #this will give only the evens

for i in range(10):
    if i==5: break
    print(i)


#Dictionaries
personid={'Alicia':'2145', 'conejo':'3658', 'carta':'1111'}
print(personid['Alicia'])


personid={'Alicia':'2145', 'conejo':'3658', 'Alicia':'1111'}
print(personid['Alicia'])## will give the last one

seq={}
seq['id1']='aaactga'
seq['id2']='aagggttcgatgcat'
print(seq['id1'])
print(seq)# the entire dictionary
seq['id1']='aaaaaaaaaaaaaaaaaaaa'#rewrite the entrance

ages={'bjorn':52, 'ana':30,'nils':46}
for key in ages:
    print(key,ages[key])

for key, value in ages.items():### will do the same
    print(key,value)

#test presence in the dictionary
if 'bjorn' in ages:
    print('bjorn is {} years old'.format(ages['bjorn']))
if 'suzan' not in ages:
    print('Suzan not in ages')
