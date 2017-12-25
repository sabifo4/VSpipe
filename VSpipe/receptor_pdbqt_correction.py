#!/usr/bin/env python
import re
import os
import sys

#split each line in the PDBQT file and check if each
#of its entries is put in the correct position, otherwise
#shift them to correct them
def correct_file(fil_read, fil_wrt):
    for line in fil_read:
        if line.startswith('ATOM'):
            columns=re.split(' ', line)
            num_col=re.split('[a-zA-Z]+|\s+', line)
            num_col=[x for x in num_col if re.search('-?[0-9]+',x)]
            [num_col.pop(0) for i in range(len(num_col)-6)]
            if (len(num_col[0])+line.index(num_col[0]))>38 or (len(num_col[1])+line.index(num_col[1]))>46 or (len(num_col[2])+line.index(num_col[2]))>54 or (len(num_col[3])+line.index(num_col[3]))>60 or (len(num_col[4])+line.index(num_col[4]))>66 or (len(num_col[5])+line.index(num_col[5]))>76:
                fil_wrt.write(line[0:11] + line[11+(len(num_col[0])+line.index(num_col[0])-38):len(line)])
            else:
                fil_wrt.write(line)
        else:
            fil_wrt.write(line)
    fil_read.close()
    fil_wrt.close()
    os.remove(sys.argv[1] + '.pdbqt')
    os.rename(sys.argv[1] + '_new.pdbqt', sys.argv[1] + '.pdbqt')

if __name__ == '__main__':
    fil_read=open(sys.argv[1] + '.pdbqt', "r")
    fil_wrt=open(sys.argv[1] + '_new.pdbqt', "w")
    correct_file(fil_read, fil_wrt)

