import sys
import my_module as mm

fasta_in = sys.argv[1]
rna_list = sys.argv[2]
fasta_out = sys.argv[3]

fasta_dict = mm.parse_fasta_to_dict(fasta_in)

with open(rna_list, 'r') as f, \
        open(fasta_out, 'w') as f2:
    short_id_dict = {}
    for key in fasta_dict:
        new_key = key.split(' ')[0]  # it was space delimited
        short_id_dict[new_key] = fasta_dict[key]
    for line in f:
        idline = line.rstrip()
        print('{}\n{}'.format(idline, short_id_dict[idline]), file=f2)
