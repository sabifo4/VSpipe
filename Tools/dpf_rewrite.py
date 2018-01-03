#!/usr/bin/env python
import sys
import os

#correct the path of the receptor PDBQT file of the GPF file
def gpf_rewrite():
    fil_r_gpf=open(sys.argv[1] + '.gpf', "r")
    fil_w_gpf=open(sys.argv[1] + '_n.gpf', "w")
    for line in fil_r_gpf:
        if line.startswith('receptor '):
            fil_w_gpf.write(line.replace('receptor ', 'receptor ' + sys.argv[2]))
        else:
            fil_w_gpf.write(line)
    fil_r_gpf.close()
    fil_w_gpf.close()
    os.remove(sys.argv[1] +'.gpf')
    os.rename(sys.argv[1] + '_n.gpf', sys.argv[1] +'.gpf')

#correct the path of the ligand PDBQT file of the DPF file
#and change the model from unbound to extended to avoid
#a warning
def dpf_rewrite():
    fil_r_dpf=open(sys.argv[1] +'.dpf', "r")
    fil_w_dpf=open(sys.argv[1] + '_n.dpf', "w")
    for line in fil_r_dpf:
        if line.startswith('move'):
            fil_w_dpf.write(line.replace('move ', 'move ' + sys.argv[3]))
        elif line.startswith('unbound_model'):
            fil_w_dpf.write(line.replace('extended', 'bound   '))
        else:
            fil_w_dpf.write(line)
    fil_r_dpf.close()
    fil_w_dpf.close()
    os.remove(sys.argv[1] +'.dpf')
    os.rename(sys.argv[1] + '_n.dpf', sys.argv[1] +'.dpf')

if __name__ == '__main__':
    gpf_rewrite()
    dpf_rewrite()
