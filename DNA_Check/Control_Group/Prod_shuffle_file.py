# coding = utf-8
# 给一个RNA_K.bed 数出里面每个序列的长度并作统计，然后再生成一个可以用来shuffle的bed文档
# 用法 ： python Prod_shuffle_file.py RNA_K.bed > result.bed

import sys
import random

def number_of_certain_probability(sequence, probability):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(sequence, probability):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item

bed_file = sys.argv[1]

with open(bed_file) as file:
	bed3 = file.readlines()

count = {}
i = 0
for element in bed3:
    element = element.split()
    L = int(element[2])-int(element[1])
    if L in count.keys():
        count[L] = count[L]+1
    else:
        count[L] = 1

strand_p = ['+','-']
numbers = []
for n in count.keys():
    # print(n)
    for i in range(count[n]):
        strand = number_of_certain_probability(strand_p,[0.5,0.5])
        print ('chr1','0', n, 'a', '0', strand,sep='\t')



