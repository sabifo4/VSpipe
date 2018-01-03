#!/usr/bin/env python
#####################################################################################
#############################Rewriting the sample.gpf################################
###############Sandra Alvarez-Carretero <sandra.ac93@gmail.com>######################
#####################################################################################
import sys
import os

#Correcting the atom types that appear in the sample.gpf taking into account the receptor.pdbqt file
def correcting_sample_gpf():
	input_file = open(sys.argv[1] + sys.argv[2] + ".pdbqt", "r") #[1] = $receptor/ // [2] = #rec_name
	output_file = open(sys.argv[1] + "atom_types.txt", "w")
	 
	list_repeated = []
	list_sorted = set()
	list_sorted_2 = []

	#Creating a list with the correct atom types and copying it into a new file "atom_types.txt"
	with output_file as out:
		with input_file as inp: 
			for line in inp:
				list_repeated.append(line[77:].rstrip())
				list_sorted.add(line[77:].rstrip())
			for atom_type in list_sorted:
				if atom_type != "":
					list_sorted_2.append(atom_type)
			for atom_type in list_sorted_2:
				out.write("%s " % atom_type) 
	#print list_sorted_2

	input_file_2 = open(sys.argv[1] + sys.argv[3], "r") # [3] = sample.gpf
	input_file_3 = open(sys.argv[1] + "atom_types.txt", "r")
	output_file_2 = open(sys.argv[1] + "n_sample.gpf", "w")
	
	#Using the "atom_types" file in order to copy the correct atom types in the new sample.gpf file called "n_sample.gpf"
	with output_file_2 as out:		
		with input_file_2 as inp:
			with input_file_3 as inp2:
				for line in inp:
					if line.startswith("npts " or "gridfld " or "spacing "):
						out.write(line)
					elif line.startswith("receptor_types "):
						for lines in inp2:
							#out.write(line.replace(line[14:37], " " + lines.rstrip() + "  " + "\n"))
							out.write(line.replace(line[14:], " " + lines.rstrip() + "\n"))
					else:
						out.write(line)
	
	#Removing the "atom_types.txt" and the old "sample.gpf files and renaming the "n_sample.gpf" file as "sample.gpf"
	os.remove(sys.argv[1] + sys.argv[3])
	os.remove(sys.argv[1] + "atom_types.txt")
	os.rename(sys.argv[1] + "n_sample.gpf", sys.argv[1] + "sample.gpf")

if __name__ == '__main__':
	correcting_sample_gpf()
