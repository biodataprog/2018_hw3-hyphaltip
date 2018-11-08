#!/usr/bin/env python3

import re

# here is function to read fasta file and return array of sequences as strings
# use it like
# sequences = read_fasta
def read_fasta (file):
    seq = ""
    fasta_pat = re.compile("^>")
    seqs = []
    with open(file, 'r') as f:
        seenheader = 0
        for line in f:
            line = line.strip()
            if fasta_pat.search(line):
                if seenheader:
                    seq = re.sub("\s+","",seq)
                    seqs.append(seq)
                    seq = ""
                seenheader = 1
            else:
                seq += line
        seq = re.sub("\s+","",seq)
        seqs.append(seq)
    return seqs


# This should read two (or more if you want the challenge) FASTA files
# Calculate Di-Nucleotide frequencies for all sequences in each file
# print out a report to compare frequencies between genomes

genome1 = "Ecoli_K-12.fasta"
genome2 = "B_subtilis_str_168.fasta"

# add your code for reading in the file
# processing the sequence to get the dinucleotide percentages
# you may want to write your own function to extract this from the
# sequences or sequence files


# you may want to change array to be dynamic if you read in files from cmdline
Header=["Motif","Ecoli_K-12","B_subtilis_str_168"]
print("\t".join(Header))
