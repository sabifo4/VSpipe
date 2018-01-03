#!/usr/bin/env python
#####################################################################################
#########Adding the metal ion information to the target protein input file###########
###############Sandra Alvarez-Carretero <sandra.ac93@gmail.com>######################
#####################################################################################
import sys
import os

#Extracts the protein's first chain, the waters previously selected with
#PyMol and the metal ion if it is a metalloproteinase
def metal_charge():
    input_file = open(sys.argv[1] + '.pdbqt', 'r')
    output_file = open(sys.argv[1] + '_n.pdbqt', 'w')
    
    with output_file as out:
        with input_file as inf:
            for line in inf:
                if line.startswith('HETATM') and sys.argv[2] in line:
                    out.write(line.replace(line[70:76], sys.argv[3]))
                else:
                    out.write(line)
    
    input_file2 = open(sys.argv[1] + '_n.pdbqt', 'r')
    output_file2 = open(sys.argv[1] + '_nn.pdbqt', 'w')
    
    with output_file2 as out2:
        with input_file2 as inf2:
            for line in inf2:
                if line.startswith('HETATM') and '+' in line and sys.argv[2] in line:
                    out2.write(line.replace('+', ' '))
                else:
                    out2.write(line)
                    
    os.remove(sys.argv[1] + '.pdbqt')
    os.remove(sys.argv[1] + '_n.pdbqt')
    os.rename(sys.argv[1] + '_nn.pdbqt', sys.argv[1] + '.pdbqt')
               
if __name__ == '__main__':
    metal_charge()
