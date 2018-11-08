#!/usr/bin/env python3

import re

# open this file
report_file = 'Ecoli-vs-Senterica.BLASTP.tab'

# print only the rows which have hit alignments 
# to accession numbers YP_008253351 -- YP_008253423 (2nd column)
# and where the 3rd column (percent identitity) is better than 25% and the 
# e-value is < 1e-10

# print an additional column to the report which lists the length of the alignment of the query

with open(report_file, "r") as blastfh:
    for line in blastfh:
        line = line.strip()
        columns = line.split("\t")
        accno = columns[1]
        percent_id = float(columns[2])

        match = re.search("(\D+)_(\d+)",accno)
#        if match:
#            print("group match 0 is ", match.group(0))
#            print("group match 1 is ", match.group(1))
#            print("group match 2 is ", match.group(2))

        split_acc = accno.split("_")
        number_for_acc = int( re.sub("\.\d+$","",split_acc[1]) )
#        print("split_acc =",split_acc)
#        print("cleaned number is ", number_for_acc)
        if( number_for_acc >= 8253351 and number_for_acc <= 8253423
            and percent_id >= 25): # filter percent ID is >= 25%
            length_aln = int(columns[7]) - int(columns[6])
#            print(length_aln)
            columns.append("%d"%(length_aln))
            print("\t".join(columns))
        
