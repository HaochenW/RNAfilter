# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 16:56:51 2020

@author: wangpeng884112
"""
import random

# Generate random "ATCG" string with length n
def random_generate(n):
    rand_dict = {1:'A',2:'C',3:'G',4:'T'}
    result = ''
    for i in range(n):
        ran_num = random.randint(1,4)
        base = rand_dict[ran_num]  #Get the random base
        result = result + base
    return result


# pair each base with the origin sequence, to make a pair sequence 
def base_pair(origin_seq):
    pair_seq = ''
    for item in origin_seq:
        if item == 'T':
            pair_seq = pair_seq + 'A'
        elif item == 'A':
            pair_seq = pair_seq + 'T'
        elif item == 'C':
            pair_seq = pair_seq + 'G'
        else:
            pair_seq = pair_seq + 'C'
    return pair_seq
            
# make each base unpair with origin sequence, to make a unpair sequence
def base_unpair(origin_seq):
    unpair_seq = ''
    for item in origin_seq:
        if item == 'T':
            rand_dict = {1:'C',2:'G',3:'T'}  # 'A' can not be used because it is pair to 'T'
            ran_num = random.randint(1,3)
            base = rand_dict[ran_num]
        elif item == 'A':
            rand_dict = {1:'C',2:'G',3:'A'}
            ran_num = random.randint(1,3)
            base = rand_dict[ran_num]
        elif item == 'C':
            rand_dict = {1:'C',2:'T',3:'A'}
            ran_num = random.randint(1,3)
            base = rand_dict[ran_num]
        else:
            rand_dict = {1:'G',2:'T',3:'A'}
            ran_num = random.randint(1,3)
            base = rand_dict[ran_num]
        unpair_seq = unpair_seq + base
    return unpair_seq
    


class RNA_sequence:
    def RAR_part(self):
        random_len1 = random.randint(5,12)
        seq1 = random_generate(random_len1) #初始茎
        
        random_len2 = random.randint(2,4)
        seq2 = random_generate(random_len2) #中间环
        
        random_len3 = random.randint(3,8)
        seq3 = random_generate(random_len3)  #顶部茎
        
        random_len4 = random.randint(2,4)   
        seq4 = random_generate(random_len4)   #顶部环
        
        seq5 = base_pair(seq3[::-1])  #顶部茎 （互补部分）
        
        seq6 = base_unpair(seq4[::-1]) + random_generate(2) #中间环
        
        seq7 = base_pair(seq1[::-1])  #初始茎互补
        
        random_len5 = random.randint(6,10)  #中间区域
        seq8 = random_generate(random_len5)
        
        RAR_seq = seq1 + seq2 + seq3 + seq4 + seq5 + seq6 + seq7 + seq8
        return RAR_seq
    
    def SL1_part(self):
        random_len6 = random.randint(2,3)
        seq9 = random_generate(random_len6)  #SL1 茎
        
        seq10 = random_generate(1) 
        
        seq11 = random_generate(2)
        
        seq12 = base_pair(seq10)
        
        seq13 = base_unpair(seq10)
        
        seq14 = base_pair(seq9[::-1])
        SL1_seq = seq9 + seq10 + seq11 + seq12 + seq13 + seq14
        return SL1_seq
    
    
    def SL2_part(self):
        random_len7 = random.randint(6,10)
        seq15 = random_generate(random_len7)
        
        random_len8 = random.randint(3,8)  # SL2 茎
        seq16 = random_generate(random_len8)
        
        random_len9 = random.randint(4,8)
        seq17 = random_generate(random_len9)
        
        seq18 = base_pair(seq16[::-1]) # SL2 茎 互补
        
        seq19 = random_generate(1)
        
        SL2_seq = seq15 + seq16 + seq17 + seq18 + seq19
        return SL2_seq

if __name__ == '__main__':
    seq_class = RNA_sequence()
    seq_num = 100
    with open('raw_sequence.fa','w') as f:
        for i in range(seq_num):
            RAR_seq = seq_class.RAR_part()
            SL1_seq = seq_class.SL1_part()
            SL2_seq = seq_class.SL2_part()
            sequence = RAR_seq + SL1_seq + SL2_seq
            f.write('>seq' + str(i) + '\n')
            f.write(sequence + '\n')
        
    




