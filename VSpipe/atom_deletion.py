#!/usr/bin/env python
import sys
import re
import os

def next(iterator):
    try:
        iternext = iterator.next.__call__
    except AttributeError:
        raise TypeError("%s object is not an iterator" % type(iterator).__name__)
    try:
        return iternext()
    except StopIteration:
        return default
#check the canonical smiles of each ligand in the SDF file and if it contains
#any of the non-supportive atoms then the ligand is erased from the file
def atom_deletion():
    fil_r_sdf=open(sys.argv[1], "r")
    cnt=0
    cn=[]
    for line in fil_r_sdf:
        if re.search('>  <cansmi>', line, re.IGNORECASE):
            cnt+=1
            atom=next(fil_r_sdf).strip()
            j=[]
            atoms=[x for x in atom if re.search('[A-Z]', x, re.IGNORECASE)]
            for i in range(len(atoms)):
                if re.search('^H$|^C$|^A$|^N$|^F$|^P$|^S$|^I$|^O$|^Z$|^G$|^J$|^Q$', atoms[i], re.IGNORECASE) or (re.search('^D$', atoms[i], re.IGNORECASE) and re.search('^H$', atoms[i-1], re.IGNORECASE)) or (re.search('^M$', atoms[i], re.IGNORECASE) and re.search('^G$', atoms[i+1], re.IGNORECASE)) or (re.search('^M$', atoms[i], re.IGNORECASE) and re.search('^N$', atoms[i+1], re.IGNORECASE)) or (re.search('^L$', atoms[i], re.IGNORECASE) and re.search('^C$', atoms[i-1], re.IGNORECASE)) or (re.search('^E$', atoms[i], re.IGNORECASE) and re.search('^F$', atoms[i-1], re.IGNORECASE)) or (re.search('^B$', atoms[i], re.IGNORECASE) and re.search('^R$', atoms[i+1], re.IGNORECASE)) or (re.search('^R$', atoms[i], re.IGNORECASE) and re.search('^B$', atoms[i-1], re.IGNORECASE)):
                    j.append(i)
            if len(j)==len(atoms):
                cn.append(cnt)    
    fil_r_sdf.close()
    cnt=1
    fil_r_sdf=open(sys.argv[1], "r")
    fil_w_sdf=open(sys.argv[2] + "del_atoms_properties_ligands.sdf", "w")
    for line in fil_r_sdf:
        if cnt in cn:
            fil_w_sdf.write(line)
        if line.startswith('$$$$')==1:
            cnt+=1
    fil_r_sdf.close()
    fil_w_sdf.close()
    
    
if __name__ == '__main__':
    atom_deletion()
