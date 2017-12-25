#!/usr/bin/env python
import sys
import os

#extract the protein's first chain from its PDB file and write it
#into a new file
def protein_extraction(a, b):
    fil_r=open(sys.argv[1], "r")
    fil_w=open(a + "_clean.pdb", "w")
    print(a + "_clean.pdb")
    for line in fil_r:
        if line.startswith('TER')==1:
                break
        if line.startswith('ATOM'):
            fil_w.write(line)
    fil_r.close()
    fil_w.close()
    return fil_w
    
if __name__ == '__main__':
    a, b=os.path.splitext(sys.argv[1])
    protein_extraction(a, b)
