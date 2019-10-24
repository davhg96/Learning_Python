#!/usr/bin/env python3
# provide 0 script 1 (seq a leer) 2(seq salida id) 3 (seq salida gc)

import sys
with open(sys.argv[1],'r') as f, open(sys.argv[2],'w') as fout:
    for line in f:
        if line.startswith('>'):
            line=line.rstrip()
            line=line.lstrip('>')
            print(line, file=fout)



with open(sys.argv[1],'r') as f, open(sys.argv[3],'w') as foutgc:
    for line in f:
        if line.startswith('>'):
            lineid=line.rstrip()

        else:
            G=line.count('G')
            C=line.count('C')
            gc=((G+C)/len(line)*100)
            GC=str(round(gc,2))
            print(lineid +' GC:'+GC+' %'+'\n'+line, end='', file=foutgc)
