# Scores alignments
def scoring(seq_dict, match=1, transition=-1, transversion=-2, g_opening=-2, g_extension=-1):  # Scores alignments
    scores = {'aa': [match], 'cc': [match], 'gg': [match], 'tt': [match],
              'ag': [transition], 'ga': [transition], 'ct': [transition], 'tc': [transition],
              'ac': [transversion], 'ca': [transversion], 'at': [transversion], 'ta': [transversion],
              'gc': [transversion], 'cg': [transversion], 'gt': [transversion], 'tg': [transversion],
              '-a': [g_opening, g_extension], 'a-': [g_opening, g_extension], '-g': [g_opening, g_extension],
              'g-': [g_opening, g_extension], '-c': [g_opening, g_extension], 'c-': [g_opening, g_extension],
              '-t': [g_opening, g_extension], 't-': [g_opening, g_extension], '--': [0, 0]}
    top_gap = ['-a', '-g', '-t', '-c', '--']
    bottom_gap = ['a-', 'g-', 't-', 'c-', '--']
    both_gap = ['--']
    scorestr = ''  # Score "matrix"
    fst_row = '  '
    for key in seq_dict:  # Initialize the first row of the "matrix"
        fst_row = '{}{}{}'.format(fst_row, '\t', key)
    scorestr = '{}{}'.format(scorestr, fst_row)

    keys_checked = []  # Combinations scored already
    for key in seq_dict:
        scorestr = '{}{}{}'.format(scorestr, '\n', key)  # Start a new row in the matrix
        for key2 in seq_dict:
            working_keys = [key, key2]  # Remember remember the key that it scores
            keys_checked.append(working_keys)
            score = 0
            row = ''
            if key == key2 or working_keys[::-1] in keys_checked:  # Check if we are scoring the same sequence
                row = '{}{}'.format(row, '\t')  # and if its the iverted alignments ie 1--2&2--1, if so put a space
                scorestr = '{}{}'.format(scorestr, row)
            else:  # Scoring procedure taking into account if the gap if opened or closed, its closed by default
                chain = [seq_dict[key2], seq_dict[key]]
                open_top_gap = False  # gap is closed by default
                open_bottom_gap = False
                for i in range(len(chain[0])):
                    pair = chain[0][i] + chain[1][i]
                    if pair in top_gap and open_top_gap is True:  # use the "opengap values if more gaps are found"
                        score += scores[pair][1]
                    if pair in bottom_gap and open_bottom_gap is True:  # use the "opengap values if more gaps are found"
                        score += scores[pair][1]
                    if pair in both_gap and open_top_gap is False and open_bottom_gap is False:
                        score += scores[pair][0]
                        open_top_gap = True
                        open_bottom_gap = True
                    if pair in top_gap and open_top_gap is False:  # if it finds a gap in the top sequence, it changes the state to open
                        score += scores[pair][0]
                        open_top_gap = True
                    if pair in bottom_gap and open_bottom_gap is False:  # if it finds a gap in the bottom sequence, it changes the state to open
                        score += scores[pair][0]
                        open_bottom_gap = True
                    elif pair not in top_gap and pair not in bottom_gap:  # If it finds a match close the gap
                        open_top_gap = False
                        open_bottom_gap = False
                        score += scores[pair][0]
                row = '{}{}{}'.format(row, '\t', score)  # add the score to the row
                scorestr = '{}{}'.format(scorestr, row)  # add the row to the "matrix"
    print(scorestr)
    return scorestr


# creates a sictionary with sequeces from a fasta file
def parse_fasta_to_dict(FASTA_file):
    seq_dict = {}
    with open(FASTA_file, 'r') as f:  # Read the input file
        for line in f:
            if line.startswith('>'):  # Save the sequences in a dictionary,
                idline = line.lstrip('>')
                idline = idline.rstrip()  # taking away the newlines
                nt = ''
            if not line.startswith('>'):
                sequence = line.rstrip()
                sequence = sequence.rstrip('\n')
                #sequence = sequence.lower()
                nt = nt + sequence
                seq_dict[idline] = nt
    return seq_dict


# counts aas in a dictionary with sequences, prints a file space delimited with the counts
def count_aa(dict_seq, fout):
    std_aminoacids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W',
                      'Y']
    aminoacid_counts = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                        'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0, 'X': 0}
    for key in dict_seq:
        peptide = dict_seq[key]
        for i in range(len(peptide) - 1):
            if peptide[i] in std_aminoacids:
                aminoacid_counts[peptide[i]] += 1
            else:
                aminoacid_counts['X'] += 1
    with open(fout, 'w') as fo:
        for key in aminoacid_counts:
            print('{} {}'.format(key, aminoacid_counts[key]), file=fo)
    return (fo)


# iterates throught a fastq file (assignment3)
def iterate_fastq(inputfile, output1, output2, output3, output4):
    with open(inputfile, 'r') as fin, \
            open(output1, 'w') as fout1, \
            open(output2, 'w') as fout2, \
            open(output3, 'w')as fout3, \
            open(output4, 'w') as fout4:
        counter = 0
        for line in fin:
            counter += 1
            if counter == 1:
                line = line.rstrip()
                idcode = line
            if counter == 2:
                line = line.rstrip()
                seq = line
            if counter == 3:
                line = line.rstrip()
                plus = line
            if counter == 4:
                line = line.rstrip()
                info = line
            if counter == 4:
                counter = 0
                if seq.startswith('TATCCTCT'):
                    print('{}\n{}\n{}\n{}'.format(idcode, seq, plus, info), file=fout1)
                elif seq.startswith('GTAAGGAG'):
                    print('{}\n{}\n{}\n{}'.format(idcode, seq, plus, info), file=fout2)
                elif seq.startswith('TCTCTCCG'):
                    print('{}\n{}\n{}\n{}'.format(idcode, seq, plus, info), file=fout3)
                else:
                    print('{}\n{}\n{}\n{}'.format(idcode, seq, plus, info), file=fout4)
    return (fout1, fout2, fout3, fout4)


# prints a fasta file from a fastqfile
def fastq_to_fasta(fastq_file, fasta_file):
    with open(fastq_file, 'r') as f_in, \
            open(fasta_file, 'w')as f_out:
        counter = 0
        for line in f_in:
            counter += 1
            if counter % 4 == 1:
                line = line.rstrip()
                line = line.lstrip('@')
                idcode = '>' + line
            if counter % 4 == 2:
                line = line.rstrip()
                seq = line
            if counter % 4 == 0:
                print('{}\n{}'.format(idcode, seq), file=f_out)


# multiline fasta to oneline fasta (files) also can create a dictionary
def oneline_fasta(FASTA_file, fileout, wantdict=True):
    if not wantdict:
        with open(FASTA_file, 'r') as f, \
                open(fileout, 'w') as fout:  # Read the input file
            nt = ''
            idline = ''
            for line in f:
                if line.startswith('>'):  # Save the sequences in a dictionary,
                    if nt:
                        print('{}\n{}'.format(idline, nt), file=fout)
                    idline = line.rstrip()  # taking away the newlines
                    idline = idline.lstrip('>')
                    nt = ''
                if not line.startswith('>'):
                    sequence = line.rstrip()
                    sequence = sequence.rstrip('\n')
                    # sequence = sequence.lower()
                    nt = nt + sequence
            print('{}\n{}'.format(idline, nt), file=fout)
    if wantdict:
        seq_dict = {}
        with open(FASTA_file, 'r') as f:
            # open(fileout, 'w') as fout:  # Read the input file
            for line in f:
                if line.startswith('>'):  # Save the sequences in a dictionary,
                    idline = line.rstrip()  # taking away the newlines
                    idline = idline.lstrip('>')
                    nt = ''
                if not line.startswith('>'):
                    sequence = line.rstrip()
                    sequence = sequence.rstrip('\n')
                    # sequence = sequence.lower()
                    nt = nt + sequence
                    seq_dict[idline] = nt
            # for key in seq_dict:
            #     print('{}\n{}'.format(key, seq_dict[key]), file=fout)
    return seq_dict


# calculate the gc content per line and prints it in the end of the id line
def GC_content_line(fasta_file, fasta_out, newfile=True, ):
    if newfile == True:
        with open(fasta_file, 'r') as f, open(fasta_out, 'w')as fout:
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


# measure the length of each line and the total lenght(printed in screen)
def seq_len_fasta(FASTA_input,FASTA_out):  # Will take a fasta in and print the total lenght in screen and a fasta with each lines lenght in the ids
    with open(FASTA_input, 'r') as f, \
            open(FASTA_out, 'w') as f2:
        nt = ''
        total_len = 0
        counter = 0
        for line in f:
            if line.startswith('>'):  # Save the sequences in a dictionary,
                if nt:
                    total_len = total_len + len(nt)
                    counter += 1
                    print('{} Len={}\n{}'.format(idline, line_len, nt), file=f2)
                idline = line.rstrip()  # taking away the newlines
                nt = ''
                line_len = 0
            if not line.startswith('>'):
                sequence = line.rstrip()
                sequence = sequence.rstrip('\n')
                nt = nt + sequence
                line_len = line_len + len(sequence)
        average_len = round(total_len / counter, 2)
        print('Total length={}\nAverage length={}'.format(total_len, average_len))


# reads a gff and gives a dictionary with a list of tuples wt the data
def get_feature_coordinates(annot_gff, target_pattern):
    result_list = []
    target = target_pattern.upper()
    with open(annot_gff, 'r') as f_in:
        for line in f_in:
            if not line.startswith('#'):
                line = line.rstrip()
                pattern = line.split('\t')
                chr_number = pattern[0]
                type_ID = pattern[2].upper()
                start = int(pattern[3])
                end = int(pattern[4])
                if target == type_ID:
                    characteristics = (chr_number, start, end)
                    result_list.append(characteristics)
    return result_list


# takes a fasta dict and coordinates and gives a dictionary with the sequences
def extract_features(genome_dict, feature_coords):
    feature_dict = {}
    for coord_tup in feature_coords:
        idline = coord_tup[0]
        start = coord_tup[1]
        end = coord_tup[2]
        seq = genome_dict[idline][start - 1:end]
        feature_dict['>{} {}-{}'.format(idline, start, end)] = seq
    return feature_dict


# prints a fasta from the previous dictionary
def dict_feature_to_fasta(feature_dict, name_fasta):
    with open(name_fasta, 'w') as f_out:
        for key in sorted(feature_dict.keys()):
            print('{}\n{}'.format(key, feature_dict[key]), file=f_out)


#takes a fasta and a target, and outputs a file with the counts for the target per line
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
