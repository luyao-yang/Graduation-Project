# -*- coding: utf-8 -*-
import sys

bed_file = sys.argv[1]

# read file
with open(bed_file) as file:
	bed3 = file.readlines()

# put blocks with the same fourth column under the same key
my_dict = {}

i=0
for bed3_line in bed3:

	my_dict[i] = bed3_line
	i = i+1	

# for each gene, print one line, caontaining block informations.
for gene_id in sorted(my_dict.keys()):
	block = my_dict[gene_id]

	# split each block(block)
	
	block_features = block.split()
	chrom = block_features[0]
	strand = '-'

	# print standard BED12 format
	print(chrom, block_features[1], block_features[2], gene_id, '0', strand,sep='\t')	

	


