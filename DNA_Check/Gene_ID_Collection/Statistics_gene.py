# coding = utf-8
# 对找到gene_id的基因种类进行统计

import sys

bed_file = sys.argv[1]
with open(bed_file) as file:
	c = file.readlines()

count = []
for line in c:
    # print(line)
    line = line.split()
    if line[5] not in count:
        # print(line[5])
        count.append(line[4])

for c in count:
    print(c)