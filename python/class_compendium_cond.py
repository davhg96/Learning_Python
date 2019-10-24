#!/usr/bin/env python3
import sys
number=int(sys.argv[1])#input the number in the comand line when selecting the .def ():
if number%3==0 and number%5==0:
    print('FizzBuzz')
elif number%5==0:
    print('Buzz')
elif number%3==0:
    print('Fizz')
else:
    print(number)
