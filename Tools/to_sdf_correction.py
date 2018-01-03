#!/usr/bin/env python
import sys
import os
import re

#put a code ID in each ligand in the SDF file when necessary
def to_sdf_correction():
    ids=[]
    #case where .smi or .can has already IDs in it 
    if sys.argv[2]=='null':
        fil_r_smi=open(sys.argv[1], 'r')
        for line in fil_r_smi:
            k=re.split('\s+', line)
            ids.append(k[1])
    fil_r=open(sys.argv[3] + '/ligands.sdf', 'r')
    fil_w=open(sys.argv[3] + '/new_ligands.sdf', 'w')
    cnt=0
    #case where .smi or .can has no IDs in it
    for line in fil_r:
        if line.startswith('$$$$')==1:
            cnt+=1
            fil_w.write('>  <code>\n')
            if sys.argv[2]!='null':
                fil_w.write(sys.argv[2] + str(cnt) + '\n\n')
            else:
                fil_w.write(ids[cnt-1] + '\n\n')
            fil_w.write('$$$$\n')
        else:
            fil_w.write(line)
    fil_r.close()
    fil_w.close()
    os.remove(sys.argv[3] + '/ligands.sdf')
    os.rename(sys.argv[3] + '/new_ligands.sdf', sys.argv[3] + '/ligands.sdf')
        
if __name__ == '__main__':
    to_sdf_correction()
