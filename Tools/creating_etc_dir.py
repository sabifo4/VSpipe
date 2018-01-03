#!/usr/bin/env python
#####################################################################################
#########Creating the "etc" directory to run the multi-node version of AD4###########
###############Sandra Alvarez-Carretero <sandra.ac93@gmail.com>######################
#####################################################################################
import os
import re
import glob
import sys

#Getting the name of the pdb files
def creating_etc_dir():
	list_pdb_names = []
	lig_dir = os.listdir(sys.argv[1]) #Pathway to the ligand directory
	
	#Creating the "docking.list" file
	output = open(sys.argv[2] + "docking.list", "w")
		
	for file in lig_dir:
		if file.endswith(".pdb"):
			lig_name = file.split('.')
			list_pdb_names.append(lig_name[0])
			output.write(list_pdb_names[0]+ "\n")
			list_pdb_names.pop(0)

	output.close()
	
if __name__ == '__main__':
	creating_etc_dir()
