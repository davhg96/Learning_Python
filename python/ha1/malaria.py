#!/usr/bin/env python3
'''
  Title: malaria.py
  Date: 2017-10-14
  Author: David Hidalgo Gil
  Description:
    This program will output a fasta file with information oftained from a
    blastx.tab file attached into the ID lines.

  List of functions:

  List of "non stadard" modules:

  Procedure:
    1. Read the fasta file and store the information in a dictionary
    2. Read the blastx.tab file and store the information (hit description)
    in a dictionary
    3. Check the lines that we want (ids should match and the information
    must not be 'null')
    4. Print a file with the fasta ids with the information selected attached
    in the end
  Usage:
    ./python3 malaria.py malaria.fna malaria.blastx.tab malaria_withIDs.fna

'''
##############################################################################
import sys
import re
fastainput=sys.argv[1]
blastxfilein=sys.argv[2]
malariafout=sys.argv[3]

if len(sys.argv) != 4:
    print("Unexpected number of arguments:", len(sys.argv)-1)
    print("Usage: ./malaria.py malaria.fna blastx.tsv output.fna")
    sys.exit(1)

fasta={}                                    # need to be outside the block to be visible for all blocks
with open(fastainput, 'r') as f:           #Read the fasta
    for line in f:                          #Seelct IDs and sequences and store into a dictionary
        if line.startswith('>'):
            id=line.rstrip()
        else:
            seq=line.rstrip()
            fasta[id]=seq
with open(blastxfilein, 'r') as f2,\
    open(malariafout,'w') as fout:          #Open the blastx file and the output file
    info={}                                 #Doesn't need to be outside
    for line2 in f2:                        #store the information in another dictionary
        line2=line2.split('\t')
        info[line2[0]]=line2[9]
    for key in fasta:
        match=re.match('>(.*?)\t',key)      #Select the Ids that match and write the output file line by line
        if not info[match.group(1)]=='null':
            print('{}\t{}{}\n{}'.format(key,'Protein=',info[match.group(1)], fasta[key]), file=fout)
