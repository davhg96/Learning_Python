"""
  Title: amino.py
  Date: 2017-10-17
  Author: David Hidalgo Gil
  Description:
    This program will retrieve sequences from a .fasta file and will count the abundance of each aminoacid (aa)

  List of functions:
    read_fasta_to_dict: this function takes a fasta file as an input and outputs a dictionary with the IDs as keys and
                        sequences as values (in lowercase)
    count_aa: This function takes a fasta file in the shape of a dictionary and outputs a file with the aminoacid
              (in 1 leter code) and the counts sepatared by spaces

  List of "non standard" modules:

  Procedure:
    1. Read the sequence .fasta file
    2. Save the information into a dictionary
    3. Count the abundance of each aa
    4. Print the counts into a file
  Usage:
    ./python3 amino.py amino.faa amino.list

"""
import sys
if len(sys.argv) != 3:
    print("Unexpected number of arguments:", len(sys.argv)-1)
    print("Usage: ./python3 amino.py amino.faa amino.list")
    sys.exit(1)
filein = sys.argv[1]
fileout = sys.argv[2]


def read_fasta_to_dict(fasta_file):
    seq_dict = {}
    with open(fasta_file, 'r') as f:  # Read the input file
        for line in f:
            if line.startswith('>'):  # Save the sequences in a dictionary,
                id = line.rstrip()  # taking away the newlines
                nt = ''
            if not line.startswith('>'):
                sequence = line.rstrip()
                sequence = sequence.rstrip('\n')
                sequence = sequence.upper()
                nt = nt + sequence
                seq_dict[id] = nt
    return seq_dict

sequences = read_fasta_to_dict(filein)

def count_aa(dict_seq, fout):
    std_aminoacids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W',
                      'Y']
    aminoacid_counts = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                        'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0, 'X': 0}
    for key in sequences:
        peptide = sequences[key]
        for i in range(len(peptide) - 1):
            if peptide[i] in std_aminoacids:
                aminoacid_counts[peptide[i]] += 1
            else:
                aminoacid_counts['X'] += 1
    with open(fout, 'w') as fo:
        for key in aminoacid_counts:
            print('{} {}'.format(key, aminoacid_counts[key]), file=fo)
    return(fo)

count_aa(sequences, fileout)
