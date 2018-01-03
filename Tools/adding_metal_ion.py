#!/usr/bin/env python
############################################################################################
#########Adding the metal ion charge information to the target protein input file###########
#####################Sandra Alvarez-Carretero <sandra.ac93@gmail.com>#######################
############################################################################################
import sys
import os

#Extracts the protein's first chain, the waters previously selected with
#PyMol and the metal ion if it is a metalloproteinase
def metal_extraction(a, b):
    input_file = open(sys.argv[1], 'r')
    output_file = open(a + '_clean.pdb', 'w')
    counter_1 = 0
    with output_file as out:
        with input_file as inf:
            for line in inf:                  
                if line.startswith('ATOM'):
                    out.write(line[0:7] + '    ' + line[11:80] + "\n")
                if line.startswith('HETATM') and sys.argv[2] in line:
                    out.write(line[0:7] + '    ' + line[11:80] + "\n")
                
    input_file2 = open(a + '_clean.pdb', 'r')
    output_file2 = open(a + '_clean_n.pdb', 'w')
    
    counter = 0

    with output_file2 as out2:
        with input_file2 as inf2:
            for line in inf2:
                counter += 1
                if line.startswith('ATOM '):
                    if len(str(counter)) == 1:
                        out2.write(line.replace('ATOM         ', 'ATOM      ' + str(counter) + '  '))
                    elif len(str(counter)) == 2:
                        out2.write(line.replace('ATOM         ', 'ATOM     ' + str(counter) + '  '))
                    elif len(str(counter)) == 3:
                        out2.write(line.replace('ATOM         ', 'ATOM    ' + str(counter) + '  '))
                    elif len(str(counter)) == 4:
                        out2.write(line.replace('ATOM         ', 'ATOM   ' + str(counter) + '  '))
            
                elif line.startswith('HETATM '):
                    if (len(str(counter)) == 1 and (sys.argv[2] in line)):
                        out2.write(line.replace('HETATM      ', 'HETATM    ' + str(counter) + ' '))
                    elif (len(str(counter)) == 2 and (sys.argv[2] in line)):
                        out2.write(line.replace('HETATM      ', 'HETATM   ' + str(counter) + ' '))
                    elif (len(str(counter)) == 3 and (sys.argv[2] in line)):
                        out2.write(line.replace('HETATM      ', 'HETATM  ' + str(counter) + ' '))
                    elif (len(str(counter)) == 4 and (sys.argv[2] in line)):
                        out2.write(line.replace('HETATM      ', 'HETATM ' + str(counter) + ' '))
    
    os.remove(a + '_clean.pdb')
    os.rename(a + '_clean_n.pdb', a + '_clean.pdb')
    print(a + "_clean.pdb") 
    return output_file2
                    
if __name__ == '__main__':
    a, b=os.path.splitext(sys.argv[1])
    metal_extraction(a, b)
