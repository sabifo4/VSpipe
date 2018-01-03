#!/usr/bin/env python
#######################################################################################
#########Generating automatically the correct docking parameter file without###########
###############################having to manually move it##############################
###############Sandra Alvarez-Carretero <sandra.ac93@gmail.com>########################
#######################################################################################
import sys
import os

def correct_dpf():
    input_file = open(sys.argv[1], 'r') #sys.argv[1] = 'receptor/sample.gpf'

    with input_file as inf:
        for line in inf:
            if line.startswith('ligand_types '):
                str1 = (line) #Getting the information of this line
            if line.startswith('gridcenter '):
                str2 = (line) 
            if line.startswith('elecmap '):
                str3 = (line)
            if line.startswith('dsolvmap '):
                str4 = (line)
    
    input_file_2 = open(sys.argv[2], 'r') #sys.argv[2] = 'pidock/scratch_sample'
    output_file = open(sys.argv[2] + '_n.dpf', 'w')
    
    with output_file as out:
        with input_file_2 as inf2:
            for line in inf2:
                if line.startswith('ligand_types '):
                    break
                out.write(line)
            out.write('{0}'.format(str1))
            out.write('fld ' + sys.argv[4] +'maps.fld                    # grid_data_file')
            out.write("\n")
    
    input_file = open(sys.argv[1], 'r') #sys.argv[1] = 'receptor/sample.dpf'
    output_file = open(sys.argv[2] + '_n.dpf', 'a') #append information
    
    with output_file as out:
        with input_file as inf:
            for line in inf:
                if line.startswith('map '):
                    out.write(line)
    
    input_file_2 = open(sys.argv[2], 'r')
    output_file = open(sys.argv[2] + '_n.dpf', 'a')
    
    with output_file as out:
        with input_file_2 as inf2:
            out.write('{0}'.format(str3))
            out.write('{0}'.format(str4))
            for line in inf2:
                if line.startswith('move '):
                    out.write(line)
                    break
            out.write('{0}'.format(str2))
            for line in inf2:
                if not (line.startswith('autodock_parameter_version 4.2 ') or line.startswith('outlev ') or line.startswith('intelec ') or line.startswith('seed ') or line.startswith('ligand_types ') or line.startswith('fld ') or line.startswith('map ') or line.startswith('elecmap ') or line.startswith('desolvmap ') or line.startswith('move ') or line.startswith('about ')):
                    out.write(line)
    
    input_file_3 = open(sys.argv[2] + '_n.dpf', 'r')
    output_file_2 = open(sys.argv[3] + 'sample.dpf', 'w')
    
    with output_file_2 as out2:
        with input_file_3 as inf3:
            for line in inf3:
                if line.startswith('fld '):
                    out2.write(line.replace('.pdb', '.'))
                if line.startswith('dsolvmap '):
                    out2.write(line.replace('dsolvmap ', 'desolvmap '))
                if line.startswith('gridcenter '):
                    out2.write(line.replace('gridcenter ', 'about '))
                if not (line.startswith('fld ') or line.startswith('dsolvmap ') or line.startswith('gridcenter ')):
                    out2.write(line)
        
    os.remove(sys.argv[2] + '_n.dpf')
    
if __name__ == '__main__':
    correct_dpf()