import sys
file_in=sys.argv[1]
file_out=sys.argv[2]

def fastq_to_fasta(fastq_file, fasta_file):
    with open(fastq_file, 'r') as f_in, \
            open(fasta_file, 'w')as f_out:
        counter = 0
        for line in f_in:
            counter += 1
            if counter % 4 == 1:
                line = line.rstrip()
                line=line.lstrip('@')
                idcode = '>'+line
            if counter % 4 == 2:
                line = line.rstrip()
                seq = line
            if counter % 4 == 0:
                print('{}\n{}'.format(idcode, seq), file=f_out)

fastq_to_fasta(file_in,file_out)