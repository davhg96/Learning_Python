#!/usr/bin/env python3

print('Exercise 1')
string=str(input('Write a sequence: '))
import re

result=[]
lc=re.findall('[a-z]', string)
uc=re.findall('[A-Z]', string)
numbers=re.findall('[0-9]', string)
wte=re.findall('. .', string)
if len(lc)!=0:
    conseq=['Contains lowercase', lc]
    result.extend(conseq)
if len(uc)!=0:
    conseq=['Contains uppercase', uc]
    result.extend(conseq)
if len(numbers)!=0:
    conseq=['Contains numbers', numbers]
    result.extend(conseq)
if len(wte)!=0:
    conseq=['Contains whithespaces', wte]
    result.extend(conseq)
if len(result)==0:
    print('Contain none of these')
print(result)



#string='aaC9 BC'
lc=re.findall('[a-z]', string)
uc=re.findall('[A-Z]', string)
numbers=re.findall('[0-9]', string)
wte=re.findall('. .', string)
found=False
if len(lc)!=0:
    print('Contains lowecase')
    found=True
if len(uc)!=0:
    print('Contains uppercase')
    found=True
if len(numbers)!=0:
    print('Contains lowecase')
    found=True
if len(wte)!=0:
    print('Contains lowecase')
    found=True
if not found:
    print('Contain none of these')
