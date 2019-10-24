#!/usr/bin/env python3
print('Exercise 1')

import sys

with open(sys.argv[1],'r') as f:
    id=set()
    counter=0
    for line in f:
        if line.startswith('>'):
            id.add(line)
            counter+=1
    if len(id)==counter:
        print('All are unique')
    else:
        print('there are some repeated ids')


print('Exercise 2 \n' )

# argv1 is the reads ids, argv2 is the reads.fna, is a fasta,
#for the fasta you need to take only the id lines and crop them to the id
import sys
import re
idset=set()
idset2=set()
with open('reads_ids.txt','r') as f:
    for line in f:
        line=line.rstrip()
        idset.add(line)
with open('reads.fna','r') as f2:
    for line in f2:
        if line.startswith('>'):
            line=line.rstrip()
            matcid=re.match('>(.*?) ',line) #dont forguet that you want to take up to the space
            idset2.add(matcid.group(1))

print(len(idset & idset2))
