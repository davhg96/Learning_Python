#Parsing 1
f=open('regions.fna', 'r')
for line in f:
    line=line.rstrip()
    print(line)
f.close()
#parsing 2, prefered way to open it
with open(sys.argv[1],,'r') as f
for line in f:
    line=line.rstrip()
    print(line)
# no need to close


import sys
f=open(sys.argv[1],'r')
print(len(sys.argv))

for line in f:
    line=line.rstrip()
    print (line)
f.close

# in case of errors we can use something like this

import sys
import os.path
if os.path.isfile(sys.argv[1]):
    sys.exit("ERROR: output file doesn't exist")
print ('Now we can open the file')
