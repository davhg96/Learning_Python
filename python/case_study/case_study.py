# 15
import sys
from my_module import oneline_fasta
from my_module import get_feature_coordinates
from my_module import extract_features
from my_module import dict_feature_to_fasta

#python3 case_study.py fungusAssembly.fna fungusAssembly.single.fna fungus_scaffold.gff CDS
#               0               1                           2               3             4
filein = sys.argv[1]
fileout = sys.argv[2]
filein2=sys.argv[3]
pattern=sys.argv[4]


genome_dict=oneline_fasta(filein, fileout, wantdict=True)
coordinates=get_feature_coordinates(filein2, pattern)
feature_fasta_dict=extract_features(genome_dict, coordinates)
dict_feature_to_fasta(feature_fasta_dict, 'feature.fasta')
