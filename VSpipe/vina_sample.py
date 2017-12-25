#!/usr/bin/env python
import sys
import os
import re

#create the config file for AutoDock Vina from the info given
#by the GPF file
def vina_sample():
    fil_r_gpf_ad4=open(sys.argv[1], "r")
    a, b=os.path.split(sys.argv[2]) #b = ID
    print(b)
    fil_w_gpf_vina=open(sys.argv[5] + "config_" + b + ".txt", "w")
    fil_w_gpf_vina.write("receptor = " + sys.argv[3] + "\n")
    fil_w_gpf_vina.write("ligand = " + sys.argv[4] + "\n") 
    for line in fil_r_gpf_ad4:
        if line.startswith('npts'):
            size=re.split('[a-zA-Z]+|\s+', line)
            size=[x for x in size if re.search('[0-9]+',x)]
        if line.startswith('gridcenter'):
            centre=re.split('[a-zA-Z]+|\s+', line)
            centre=[x for x in centre if re.search('-?[0-9]+.?',x)]
    fil_w_gpf_vina.write("center_x = " + centre[0] +"\n")
    fil_w_gpf_vina.write("center_y = " + centre[1] +"\n")
    fil_w_gpf_vina.write("center_z = " + centre[2]+"\n")
    #########################################################################
    #####MODIFICATION-March15-SA-The space sizes cannot be in "grid points"
    #####like in AD4. They must be in Angstroms so they have to be multiplied
    #####by 0.375#############################################################
    #####Before:
    #fil_w_gpf_vina.write("size_x = " + size[0] +"\n")
    #fil_w_gpf_vina.write("size_y = " + size[1] +"\n")
    #fil_w_gpf_vina.write("size_z = " + size[2] +"\n")
    #####Now:
    size0 = float(size[0])*0.375
    size1 = float(size[1])*0.375
    size2 = float(size[2])*0.375
    fil_w_gpf_vina.write("size_x = " + str(size0) +"\n")
    fil_w_gpf_vina.write("size_y = " + str(size1) +"\n")
    fil_w_gpf_vina.write("size_z = " + str(size2) +"\n")

    fil_w_gpf_vina.write("out = " + sys.argv[6] + b + "_vina.pdbqt")
    fil_r_gpf_ad4.close()
    fil_w_gpf_vina.close()

if __name__ == '__main__':
    vina_sample()

#sys.argv[1] = sample.gpf
#sys.argv[2] = filename (b = ID)
#sys.argv[3] = name_receptor.pdbqt 
#sys.argv[4] = results/pdbqt_lip_rules/'ID_name_of_file'.pdbqt
#sys.argv[5] = results/config_vina
#sys.argv[6] = results/vina_pdbqt
