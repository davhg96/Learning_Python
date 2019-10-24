"""
  Title: score.py
  Date: 2017-10-14
  Author: David Hidalgo Gil
  Description:
    This program will score sequence alignments, the sequences must have the same length

  List of functions:
    read_fasta_to_dict: this function takes a fasta file as an input and outputs a dictionary with the IDs as keys and
                        sequences as values (in lowercase)
    scoring: takes sequences in a dictionary and scores for match, gap opening, gap extension, transitions and
             transversions

  List of "non standard" modules:

  Procedure:
    1. Read the alignment fasta file
    2. Save the information into a dictionary
    3. Retrieve the sequences in pairs from the Dictionary
    4. Score the alignments
    5. Print the answer (score)
  Usage:
    ./python3 score.extra.py -1 -2 -2 -1 1 score.extra.fna

"""
#!/usr/bin/env python3
import sys

transition = int(sys.argv[1])
transversion = int(sys.argv[2])
g_opening = int(sys.argv[3])
g_extension = int(sys.argv[4])
match = int(sys.argv[5])
fileinput = sys.argv[6]

if len(sys.argv) != 6:
    print("Unexpected number of arguments:", len(sys.argv)-1)
    print("Usage: ./python3 score.extra.py -1 -2 -2 -1 1 score.extra.fna, numbers are for transitions, "
          "transversions, gap openong, gap extension and match")
    sys.exit(1)


def read_fasta_to_dict(FASTA_file):
    seq_dict = {}
    with open(FASTA_file, 'r') as f:  # Read the input file
        for line in f:
            if line.startswith('>'):  # Save the sequences in a dictionary,
                id = line.rstrip()  # taking away the newlines
                nt = ''
            if not line.startswith('>'):
                sequence = line.rstrip()
                sequence = sequence.rstrip('\n')
                sequence = sequence.lower()
                nt = nt + sequence
                seq_dict[id] = nt
    return seq_dict


def scoring(seq_dict, match=1, transition=-1, transversion=-2, g_opening=-2, g_extension=-1):
    scores = {'aa': [match], 'cc': [match], 'gg': [match], 'tt': [match],
              'ag': [transition], 'ga': [transition], 'ct': [transition], 'tc': [transition],
              'ac': [transversion], 'ca': [transversion], 'at': [transversion], 'ta': [transversion],
              'gc': [transversion], 'cg': [transversion], 'gt': [transversion], 'tg': [transversion],
              '-a': [g_opening, g_extension], 'a-': [g_opening, g_extension], '-g': [g_opening, g_extension],
              'g-': [g_opening, g_extension], '-c': [g_opening, g_extension], 'c-': [g_opening, g_extension],
              '-t': [g_opening, g_extension], 't-': [g_opening, g_extension], '--': [0,0]}
    top_gap = ['-a', '-g', '-t', '-c', '--']
    bottom_gap = ['a-', 'g-', 't-', 'c-', '--']
    both_gap=['--']
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
                        open_top_gap= True
                        open_bottom_gap=True
                    if pair in top_gap and open_top_gap is False:  #if it finds a gap in the top sequence, it changes the state to open
                        score += scores[pair][0]
                        open_top_gap = True
                    if pair in bottom_gap and open_bottom_gap is False:  # if it finds a gap in the bottom sequence, it changes the state to open
                        score += scores[pair][0]
                        open_bottom_gap = True
                    elif pair not in top_gap and pair not in bottom_gap:  # If it finds a match close the gap
                        open_top_gap = False
                        open_bottom_gap= False
                        score += scores[pair][0]
                row = '{}{}{}'.format(row, '\t', score)  # add the score to the row
                scorestr = '{}{}'.format(scorestr, row)  # add the row to the "matrix"
    print(scorestr)
    return scorestr


scoring(read_fasta_to_dict(fileinput), match, transition, transversion, g_opening, g_extension)
