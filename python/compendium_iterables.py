#!/usr/bin/env python3
## exercise 1
import sys
numbers=input('Please write some numbers separated by ",": ')
numbers=numbers.split(',')

result=(0)
for i in numbers:
    i=int(i)
    result=result+i

print(result)


#exercise 2
import itertools
nucleotides=['A','C','G','T']
codons=list(itertools.product(nucleotides,repeat=3))
print(codons)
# every codon will be a tuple,
type(codons[1])


#Exercise 3
# leucine= TTA TTG CTT CTC CTA CTG
leu_codons=[('TTA'),('TTG'),('CTT'),('CTC'),('CTA'),('CTG')]
for i in range(len(codons)):
    str=''.join(codons[i])
    for c in range(len(leu_codons)):
            if str==leu_codons[c]:
                print('This codon translate to leucine', codons[i])

#########################
print('another way of doing 2 and 3')
print('2')
nts=['A','T','C','G']
codon=list()
for nt1 in nts:
    for nt2 in nts:
        for nt3 in nts:
            codon.append('{}{}{}'.format(nt1,nt2,nt3))


print('exercise 3')
for i in codon:
    for c in leu_codons:
            if i==c:
                print('This codon translate to leucine', i)
