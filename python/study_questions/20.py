import sys

input = sys.argv[1]
target = sys.argv[2]
f_out=sys.argv[3]

def oligo_line_counter(FASTA_input, target, file_out):
    with open(FASTA_input, 'r') as f, \
            open(file_out, 'w')as f2:
        import re
        headers = False
        if not headers:
            print('#oligo:\t {}\n#id\tabundance'.format(target), file=f2)
        headers = True
        if headers:
            target = str(target + 'i' + '?')
            target = target.lower()

            nt = ''
            for line in f:
                if line.startswith('>'):  # Save the sequences in a dictionary,
                    if nt:
                        counts = len(re.findall(target,nt))
                        print('{}\t{}'.format(id, counts), file=f2)
                    idline = line.rstrip()  # taking away the newlines
                    idline = idline.lstrip('>')
                    id = idline.split('\t')[0]
                    nt = ''
                if not line.startswith('>'):
                    sequence = line.rstrip()
                    sequence = sequence.rstrip('\n')
                    sequence = sequence.lower()
                    nt = nt + sequence

oligo_line_counter(input,target,f_out)
