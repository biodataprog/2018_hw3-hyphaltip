#!/usr/bin/env python3
import re
protein_file = 'Saccharomyces_cerevisiae.pep'

# Your solution should print out the aggregate frequency of each amino acid across all the sequences in the file

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


# add your code for reading in the file
# processing the sequence to get the amino acid counts and overall
# percentage

sequences = read_fasta("Saccharomyces_cerevisiae.pep")
#print(sequences)
amino_acids = {}
total = 0
for seq in sequences:
    for aa in seq:
        total += 1
        if aa in amino_acids:
            amino_acids[aa] += 1
        else:
            amino_acids[aa] = 1


Header = ["Amino Acid","Proteome Percentage"]
print("\t".join(Header))

for aa in sorted(amino_acids.keys()):
    #print("\t".join([ aa, str(100 * amino_acids[aa]/total) ] ))
    print("%s\t%.2f %%"%(aa,100 * (amino_acids[aa] / total) ) )
    # your code for the report
