#!/usr/bin/env python3
'''
  Title: score.py
  Date: 2017-10-14
  Author: David Hidalgo Gil
  Description:
    This program will score sequence alignments, the sequences must have the same length

  List of functions:

  List of "non standard" modules:

  Procedure:
    1. Read th ealignment fasta file
    2. Save th einformation into a dictionary
    3. Retrieve th esequences in pairs from the Dictionary
    4. Score the alignments
    5. Print the answer (score)
  Usage:
    ./python3 score.py score.fna

'''
##############################################################################


import sys

if len(sys.argv) != 2:
    print("Unexpected number of arguments:", len(sys.argv)-1)
    print("Usage: ./python3 score.extra.py score.extra.fna")
    sys.exit(1)
filein=sys.argv[1]
seq={}
match=1
transition=-1
transversion=-2
gap=-1

with open(filein, 'r') as f:               #Read the input file
    str=''
    for line in f:
        if line.startswith('>'):                #Save the sequences in a dictionary,
            id=line.rstrip()                    # taking away the newlines
            nt=''
        if not line.startswith('>'):
            sequence=line.rstrip()
            sequence=sequence.rstrip('\n')
            sequence=sequence.lower()
            nt=nt+sequence
            seq[id]=nt

score=0

scores={'aa':match,'cc':match,'gg':match, 'tt':match,\
'ag':transition,'ga':transition,'ct':transition,'tc':transition,\
'ac':transversion,'ca':transversion,'at':transversion,'ta':transversion,\
'gc':transversion,'cg':transversion,'gt':transversion,'tg':transversion,\
'-a':gap,'a-':gap,'-g':gap,'g-':gap,'-c':gap,\
'c-':gap,'-t':gap,'t-':gap,'--':gap}            #Dictionary with scores

chain=[]                                        #list with the sequences
for key in seq:
    chain.append(seq[key])

for i in range(len(chain[0])):                  #Scoring procedure, make a 2nt string
    pair=chain[0][i]+chain[1][i]                #and look for it in the score dictionary
    score+=scores[pair]
print(score)
