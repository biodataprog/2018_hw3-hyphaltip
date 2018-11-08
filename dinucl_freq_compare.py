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

ecoliK = read_fasta(genome1)
bsub = read_fasta(genome2)
print("there are ", len(ecoliK),"chromosome(s) in this file")

di_counts_ecoli = {}
total_ecoli = 0
for sequence in ecoliK:
    for index in range(0,len(sequence)-1,1):
        di = sequence[index:index+2]
        if di in di_counts_ecoli:
            total_ecoli += 1 
            di_counts_ecoli[di] += 1
        else:
            di_counts_ecoli[di] = 1

di_counts_bsub = {}
total_bsub = 0
for sequence in bsub:
    for index in range(0,len(sequence)-1):
        di = sequence[index:index+2]
        if di in di_counts_bsub:
            total_bsub += 1
            di_counts_bsub[di] += 1
        else:
            di_counts_bsub[di] = 1

    
# you may want to change array to be dynamic if you read in files from cmdline
Header=["Motif","Ecoli_K-12","B_subtilis_str_168"]
print("\t".join(Header))
for di in sorted(di_counts_ecoli.keys()):
    print("%s\t%.2f %%\t%.2f %%"%(di,
                         100 * di_counts_ecoli[di] / total_ecoli,
                         100 * di_counts_bsub[di] / total_bsub))
