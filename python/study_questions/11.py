#11
import sys
file=sys.argv[1]
# def sequece_counter(file):
with open(file, 'r') as file_in:
    sequencecounter = 0
    if file.endswith('.fastq'):
        counter = 0

        for line in file_in:
                counter += 1
                if counter%4 == 2:
                    sequencecounter+=1
    else:
        for line in file_in:
            if line.startswith('>'):
                pass
            else:
                sequencecounter+=1
    print(sequencecounter)
    # return sequencecounter



