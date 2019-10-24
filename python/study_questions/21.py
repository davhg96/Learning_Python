import sys

file_in = sys.argv[1]
file_out = sys.argv[2]


def translator_DNA_to_AA(FASTA_in, FASTA_out):
    with open(FASTA_in, 'r') as f, \
            open(FASTA_out, 'w')as f2:
        codon2aa = {"AAA": "K", "AAC": "N", "AAG": "K", "AAU": "N",
                    "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
                    "AGA": "R", "AGC": "S", "AGG": "R", "AGU": "S",
                    "AUA": "I", "AUC": "I", "AUG": "M", "AUU": "I",
                    "CAA": "Q", "CAC": "H", "CAG": "Q", "CAU": "H",
                    "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
                    "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
                    "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
                    "GAA": "E", "GAC": "D", "GAG": "E", "GAU": "D",
                    "GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
                    "GGA": "G", "GGC": "G", "GGG": "G", "GGU": "G",
                    "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
                    "UAA": "_", "UAC": "Y", "UAG": "_", "UAU": "T",
                    "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
                    "UGA": "_", "UGC": "C", "UGG": "W", "UGU": "C",
                    "UUA": "L", "UUC": "F", "UUG": "L", "UUU": "F"}
        nt = ''
        translation = ''
        for line in f:
            if line.startswith('>'):  # Save the sequences in a dictionary,
                if nt:
                    counter = 0
                    nt = nt.replace('T', 'U')
                    for i in nt:
                        if not counter == 2:
                            triplet = triplet + i
                            counter += 1
                        else:
                            counter = 0
                            triplet = triplet + i
                            translation = translation + codon2aa[triplet]
                            triplet = ''

                    print('{}\n{}'.format(idline, translation), file=f2)
                idline = line.rstrip()  # taking away the newlines
                triplet = ''
                translation = ''
                nt = ''
            if not line.startswith('>'):
                sequence = line.rstrip()
                sequence = sequence.rstrip('\n')
                sequence = sequence.upper()
                nt = nt + sequence


translator_DNA_to_AA(file_in, file_out)
