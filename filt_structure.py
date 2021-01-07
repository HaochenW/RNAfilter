# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:08:25 2021

@author: wangpeng884112
"""
import pandas as pd
import numpy as np

# 阅读RNAfold软件的输出文件，以Dataframe形式输出；
def read_info(file):
    sequence = []
    structure = []
    with open(file,'r') as f:
        for i,item in enumerate(f):
            if (i+2) % 3 == 0:
                sequence.append(item.strip('\n'))
            elif (i+1) % 3 == 0:
                structure.append(item.strip('\n').split('. ')[0])
    info = {'seq':sequence, 'structure':structure}
    df = pd.DataFrame(data=info)
    return df

# 定义括号栈
class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        进栈函数
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈函数，
        """
        return self.stack.pop()

    def gettop(self):
        """
        取栈顶
        """
        return self.stack[-1]
    


# 找到每个RNAfold结构/子结构有几个分开的子结构，给出起始与终止位置；
# 输入：structure - RNAfold结构
# 输出：start,end：每个子结构的开始与终止位置；        
def find_start_end(structure):
    structure_stack = Stack()
    end = []
    start = []
    record_flag = 0  #为保证只记录第一个栈为空的位点，加入这个flag;
    i = 0 
    while True:
        try:
            if structure[i] == '(' and structure_stack.stack == []:
                start.append(i)  #找到开始位置
            if structure[i] == '(':
                structure_stack.push(structure[i])
            elif structure[i] == ')':
                structure_stack.pop()
            
            if structure_stack.stack == [] and record_flag == 1:
                end.append(i)  #找到终止位置
                record_flag = 0
            if structure_stack.stack != []:
                record_flag = 1
            i = i + 1
        except:
            break
    return start,end

# 将最外层的匹配(的括号)全部剥离
def peel(structure):
    while True:
        if structure[0] == '(' and structure[-1] == ')':
            structure = structure[i+1:len(structure)-1]
        else:
            break
    return structure



file = 'structure.str'
info = read_info(file)

flag_record = np.zeros((len(info)))
for index, row in info.iterrows():
    structure = row.structure.split(' ')[0]
    start,end = find_start_end(structure)
    if len(start) != 3:
        continue
    if end[0] == start[1] - 1:  #不同结构中间有间隔
        continue
    elif end[1] == start[2] - 1: #不同结构中间有间隔
        continue
    for i in range(len(start)):
        sub_structure = structure[start[i]:end[i]+1] # 由于python机制，需要+1
        sub_structure = peel(sub_structure)
        if i == 0 or i == 1:  ##RAR结构判定
            if '(' in sub_structure:
                sub_start,sub_end = find_start_end(sub_structure)
                if len(sub_start) != 1:
                    continue
                sub_sub_structure = sub_structure[sub_start[0]:sub_end[0]+1]
                sub_sub_structure = peel(sub_sub_structure)
                if '(' in sub_sub_structure:
                    continue
            else:
                continue
        if i == 2:
            if '(' in sub_structure:
                continue
        flag_record[index] = 1
    if index == 15:
        break
    


with open('filter_seq.fa','w') as f:
    i = 0
    for index,row in info.iterrows():
        if flag_record[index] == 1:
            f.write('>' + str(i) + '\n')
            f.write(row.seq + '\n')
            i = i + 1
            


















    

