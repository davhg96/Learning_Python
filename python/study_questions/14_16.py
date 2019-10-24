import sys
file_input=sys.argv[1]
file_out=sys.argv[2]

def seq_len_fasta(FASTA_input,FASTA_out):#Will take a fasta in and print the total lenght in screen and a fasta with each lines lenght in the ids
    with open(FASTA_input, 'r') as f,\
         open(FASTA_out,'w') as f2:
        nt=''
        total_len=0
        counter=0
        for line in f:
            if line.startswith('>'):  # Save the sequences in a dictionary,
                if nt:
                    total_len=total_len+len(nt)
                    counter+=1
                    print('{} Len={}\n{}'.format(idline,line_len,nt), file=f2)
                idline = line.rstrip()  # taking away the newlines
                nt = ''
                line_len=0
            if not line.startswith('>'):
                sequence = line.rstrip()
                sequence = sequence.rstrip('\n')
                nt = nt + sequence
                line_len = line_len+len(sequence)
        average_len=round(total_len/counter,2)
        print('Total length={}\nAverage length={}'.format(total_len,average_len))


seq_len_fasta(file_input,file_out)