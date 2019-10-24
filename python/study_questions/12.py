import sys
fileinput=sys.argv[1]
with open (fileinput,'r') as file_in:
    seq=''
    for line in file_in:
        if line.startswith('>'):
            idline=line.rstrip()
        else:
            seq=line.rstrip()
            seq=seq.replace('T','U')
        print(idline,'\n', seq)