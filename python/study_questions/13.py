import sys

file_input = sys.argv[1]
file_out = sys.argv[2]


def GC_content_line(fasta_file, fasta_out, newfile=True ):
    if newfile == True:
        with open(fasta_file, 'r') as f, open(fasta_out,'w')as fout:
            nt = ''
            idline = ''
            for line in f:
                if line.startswith('>'):  # Save the sequences in a dictionary,
                    if nt:
                        G = nt.count('G')
                        C = nt.count('C')
                        GC = str(round(((G + C) / len(nt) * 100), 2))
                        print('{}\tGC%={}\n{}'.format(idline, GC, nt), file=fout)
                    idline = line.rstrip()  # taking away the newlines
                    idline = idline.lstrip('>')
                    nt = ''
                if not line.startswith('>'):
                    sequence = line.rstrip()
                    sequence = sequence.rstrip('\n')
                    sequence = sequence.upper()
                    nt = nt + sequence
    else:
        with open(fasta_file, 'r') as f:
            nt = ''
            idline = ''
            for line in f:
                if line.startswith('>'):  # Save the sequences in a dictionary,
                    if nt:
                        G = nt.count('G')
                        C = nt.count('C')
                        GC = str(round(((G + C) / len(nt) * 100), 2))
                        print('{}\tGC%={}\n{}'.format(idline, GC, nt))
                    idline = line.rstrip()  # taking away the newlines
                    idline = idline.lstrip('>')

                    nt = ''
                if not line.startswith('>'):
                    sequence = line.rstrip()
                    sequence = sequence.rstrip('\n')
                    sequence = sequence.upper()
                    nt = nt + sequence


GC_content_line(file_input, file_out, newfile=True)
