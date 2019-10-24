"""
  Title: barcode.py
  Date: 2017-10-17
  Author: David Hidalgo Gil
  Description:
    This program will retrieve sequences from a .fasta and will sort the sequences by barcode,
    ignoring the sequences without any barcode.

  List of functions:

  List of "non standard" modules:

  Procedure:
    1. Read the sequence .fasta file
    2. Save the information into a dictionary
    3. Count the abundance of each aa
    4. Print the counts into a file
  Usage:
    ./python3 barcode.py barcode.fastq

"""
import sys
if len(sys.argv) != 2:
    print("Unexpected number of arguments:", len(sys.argv)-1)
    print("Usage: ./python3 barcode.py barcode.fastq")
    sys.exit(1)
inputfile = sys.argv[1]
with open(inputfile, 'r') as fin, \
     open('sample1.fastq', 'w') as fout1, \
     open('samle2.fastq', 'w') as fout2, \
     open('sample3.fastq', 'w')as fout3, \
     open('undetermined.fastq', 'w') as fout4:
    counter = 0
    for line in fin:
        counter += 1
        if counter == 1:
            line = line.rstrip()
            idcode = line
        if counter == 2:
            line = line.rstrip()
            seq = line
        if counter == 3:
            line = line.rstrip()
            plus = line
        if counter == 4:
            line = line.rstrip()
            info = line
        if counter == 4:
            counter = 0
            if seq.startswith('TATCCTCT'):
                print('{}\n{}\n{}\n{}'.format(idcode, seq, plus, info), file=fout1)
            elif seq.startswith('GTAAGGAG'):
                print('{}\n{}\n{}\n{}'.format(idcode, seq, plus, info), file=fout2)
            elif seq.startswith('TCTCTCCG'):
                print('{}\n{}\n{}\n{}'.format(idcode, seq, plus, info), file=fout3)
            else:
                print('{}\n{}\n{}\n{}'.format(idcode, seq, plus, info), file=fout4)
