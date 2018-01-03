#!/usr/bin/env python
import sys
import csv
import re
import os
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import shutil
import errno

###MODIFICATION-SA-Jun-15-Copying filtered ligands files to the filtered_results directory #######################
###In case you filter the results, this function copies the ligands files into the "filtered_results" directory###
def copy(src, dest):
	try:
		shutil.copytree(src, dest)
	except OSError as e:
		#If the error was casued because the source wasn't a directory
		if e.errno == errno.ENOTDIR:
			shutil.copy(src, dst)
		else:
			print("Directory not copied. Error %s" % e)
##################################################################################################################

####MODIFICATION-SA-1-JUN-15-PLOTTING#############################################################################
####This function plots the information found in the csv file and saves the plots in the "results" directory if###
####results have not been filtered or in the "filtered_results" directory if results have been filtered###########
#Lists for the coordinates needed to plot
def plot(a, b):
    #a = csv_to_read | b = filtered_results/
    BEI = [] 
    SEI = [] 
    NSEI = []
    NBEI = []
    nBEI = []
    PSA = []
    MW = []
    logP = []
    HBD = []
    HBA = []
    compounds_list = []
 
    #with fil_r_csv as inp1:
    with a as inp1:
	for line in inp1:
		if line.startswith("Smiles")==0:
			reader = csv.reader(inp1, delimiter=",")

			for line in reader:
				BEI.append(line[12])
				SEI.append(line[13])
				NSEI.append(line[14])
				NBEI.append(line[15])
				nBEI.append(line[16])
				PSA.append(line[7])
				MW.append(line[2])
                                logP.append(line[4])
                     		HBD.append(line[5])
				HBA.append(line[6])

    compounds_number = (len(MW) + 1)
    compounds_list = range(1, compounds_number)

    #PLOT NSEI vs nBEI
    plot1 = plt.scatter(NSEI, nBEI)
    plot1 = plt.xlabel("NSEI", fontsize=12)
    plot1 = plt.ylabel("nBEI", fontsize = 12)
    plot1 = plt.title("NSEI-nBEI")
    if filt=='0':
    	plot1 = plt.savefig(sys.argv[1] + "NSEI-nBEI.pdf")
    if filt=='1':
	plot1 = plt.savefig(sys.argv[1] + b + "NSEI-nBEI.pdf")
    plot1 = plt.close()

    #PLOT SEI vs BEI
    plot2 = plt.scatter(SEI, BEI)
    plot2 = plt.xlabel("SEI", fontsize=12)
    plot2 = plt.ylabel("BEI", fontsize = 12)
    plot2 = plt.title("SEI-BEI")
    if filt=='0':
    	plot2 = plt.savefig(sys.argv[1] + "SEI-BEI.pdf")
    if filt=='1':
	plot2 = plt.savefig(sys.argv[1] + b + "SEI-BEI.pdf")
    plot2 = plt.close()

    #Converting MW data in float numbers
    MW_float = []
    for i in MW:
	MW_float.append(float(i))

    MW_100 = []
    MW_200 = []
    MW_300 = []
    MW_400 = []
    MW_400_1 = []
    
    for i in MW_float:
	if i < float(100):
		MW_100.append(i)
	elif ((i >= float(100)) and (i < float(200))):
		MW_200.append(i)
	elif ((i >= float(200)) and (i < float(300))):
		MW_300.append(i)
	elif ((i >= float(300)) and (i < float(400))):
		MW_400.append(i)
	else:
		MW_400_1.append(i)

    #Y-values, the number of compounds in that range
    Y_values = [len(MW_100), len(MW_200), len(MW_300), len(MW_400), len(MW_400_1)]
    #X-values, the range
    X_values = [100, 200, 300, 400, 500]
    #PLOT MW vs compounds
    plot3 = plt.bar(X_values, Y_values, 30.0)
    plot3 = plt.xlabel("MW range", fontsize=12)
    plot3 = plt.ylabel("Number of compounds", fontsize = 12)
    plot3 = plt.title("MW-Frequency")
    plot3 = plt.xlim(0, 600)
    plot3 = plt.xticks((115, 215, 315, 415, 515, 615), ('<100', '100-200', '200-300', '300-400', '>= 400', ' '))
    if filt=='0':
    	plot3 = plt.savefig(sys.argv[1] + "MW-Frequency.pdf")
    elif filt=='1':
	plot3 = plt.savefig(sys.argv[1] + b + "MW-Frequency.pdf")
    plot3 = plt.close()

    #PLOT PSA vs compounds
    #Converting PSA data in float numbers
    PSA_float = []
    for i in PSA:
	PSA_float.append(float(i))

    PSA_50 = []
    PSA_100 = []
    PSA_150 = []
    PSA_200 = []
    PSA_200_1 = []
    
    for i in PSA_float:
	if i < float(50):
		PSA_50.append(i)
	elif ((i >= float(50)) and (i < float(100))):
		PSA_100.append(i)
	elif ((i >= float(100)) and (i < float(150))):
		PSA_150.append(i)
	elif ((i >= float(150)) and (i < float(200))):
		PSA_200.append(i)
	else:
		PSA_200_1.append(i)

    #Y-values, the number of compounds in that range
    Y_values = [len(PSA_50), len(PSA_100), len(PSA_150), len(PSA_200), len(PSA_200_1)]
    #X-values, the range
    X_values = [50, 100, 150, 200, 250]
    plot4 = plt.bar(X_values, Y_values, 30.0)
    plot4 = plt.xlabel("PSA range", fontsize=12)
    plot4 = plt.ylabel("Number of compounds", fontsize = 12)
    plot4 = plt.title("PSA-Number of compounds")
    plot4 = plt.xlim(0, 300)
    plot4 = plt.xticks((65, 115, 165, 215, 265, 315), ('<50', '50-100', '100-150', '150-200', '>= 200', ' '))
    if filt=='0':
    	plot4 = plt.savefig(sys.argv[1] + "PSA.pdf")
    elif filt=='1':
	plot4 = plt.savefig(sys.argv[1] + b + "PSA.pdf")
    plot4 = plt.close()
    
    #PLOT logP vs compounds
    #Converting logP data in float numbers
    logP_float = []
    for i in logP:
	logP_float.append(float(i))

    logP_1 = []
    logP_2 = []
    logP_3 = []
    logP_4 = []
    logP_5 = []
    logP_5_1 = []

    
    for i in logP_float:
	if i < float(1):
		logP_1.append(i)
	elif ((i >= float(1)) and (i < float(2))):
		logP_2.append(i)
	elif ((i >= float(2)) and (i < float(3))):
		logP_3.append(i)
	elif ((i >= float(3)) and (i < float(4))):
		logP_4.append(i)
	elif ((i >= float(4)) and (i < float(5))):
		logP_5.append(i)
        else:
		logP_5_1.append(i)

    #Y-values, the number of compounds in that range
    Y_values = [len(logP_1), len(logP_2), len(logP_3), len(logP_4), len(logP_5), len(logP_5_1)]
    #X-values, the range
    X_values = [1, 2, 3, 4, 5, 6]
    #PLOT logP vs compounds
    plot5 = plt.bar(X_values, Y_values, 0.5)
    plot5 = plt.xlabel("logP range", fontsize=12)
    plot5 = plt.ylabel("Number of compounds", fontsize = 12)
    plot5 = plt.title("logP-Number of compounds")
    plot5 = plt.xlim(0, 7)
    plot5 = plt.xticks((1.25, 2.25, 3.25, 4.25, 5.25, 6.25, 7.25), ('<1', '1-2', '2-3', '3-4', '4-5', '>= 5', ' '))
    if filt=='0':
    	plot5 = plt.savefig(sys.argv[1] + "logP.pdf")
    elif filt=='1':
	plot5 = plt.savefig(sys.argv[1] + b + "logP.pdf")
    plot5 = plt.close()

    #PLOT number of HBA vs Number of compounds
    #Converting HBA data in int numbers
    HBA_float = []
    HBA_int = []
    for i in HBA:
	HBA_float.append(float(i))
    for i in HBA_float:
	HBA_int.append(int(i))

    HBA_0 = []
    HBA_1 = []
    HBA_2 = []
    HBA_3 = []
    HBA_4 = []
    HBA_5 = []
    HBA_6 = []
    HBA_7 = []
    HBA_8 = []
    HBA_9_1 = []

    for i in HBA_int:
	if i == int(0):
		HBA_0.append(i)
	elif i == int(1):
		HBA_1.append(i)
	elif i == int(2):
		HBA_2.append(i)
	elif i == int(3):
		HBA_3.append(i)
	elif i == int(4):
		HBA_4.append(i)
	elif i == int(5):
		HBA_5.append(i)
	elif i == int(6):
		HBA_6.append(i)
	elif i == int(7):
		HBA_7.append(i)
	elif i == int(8):
		HBA_8.append(i)
	else:
		HBA_9_1.append(i)

    #X-values, the number of compounds in that range
    Y_values = [len(HBA_0), len(HBA_1), len(HBA_2), len(HBA_3), len(HBA_4), len(HBA_5), len(HBA_6), len(HBA_7), len(HBA_8), len(HBA_9_1)]
    #X-values, the range
    X_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #PLOT HBA vs compounds
    plot6 = plt.bar(X_values, Y_values, 0.5)
    plot6 = plt.xlabel("Number of HBA", fontsize=12)
    plot6 = plt.ylabel("Number of compounds", fontsize = 12)
    plot6 = plt.title("Number of HBA-BEI")
    plot6 = plt.xlim(0, 11)
    plot6 = plt.xticks((0.25, 1.25, 2.25, 3.25, 4.25, 5.25, 6.25, 7.25, 8.25, 9.25, 10.25), ('0', '1', '2', '3', '4', '5', '6', '7', '8', '>= 9', ' '))
    plot6 = plt.savefig(sys.argv[1] + "HBA-Number of compounds.pdf")
    if filt=='0':
    	plot6 = plt.savefig(sys.argv[1] + "HBA-Number of compounds.pdf")
    elif filt=='1':
	plot6 = plt.savefig(sys.argv[1] + b + "HBA-Number of compounds.pdf")
    plot6 = plt.close()

#################################################################################################################################################



#parse each line in the output file and remove the one that has a user-chosen entry that
#does not abide by the threshold of the user
def filtering(a, choice, filt):
	## 170203--Define a counter and a new array to save filtered pdb info ##
	counter = 0
	filtered_ids = []
	## 170203--END OF MODIFICATION ##
	lines=[]
	ids=[]
	## Read txt file and create a new output file to save 
	## the filter decisions
	#fil_r_txt=open(sys.argv[1] + "output.txt", "r")
	fil_r_txt=open(sys.argv[1] + "output.tsv", "r")
	fil_w_txt=open(sys.argv[1] + "n_output.txt", "w")
	for line in fil_r_txt:
		## If it is not a header...
		if line.startswith('Smiles')==0:
			cells=re.split('\t', line.strip())
#####MODIFICATION-SA-APR-Modification to obtain the output file when MPI is run as there are some compounds that do not dock and not all lines are inside###
			if len(cells) != 9:
				for i in range(16):
					if cells[i+2] != 'Null':
						cells[i+2]=float(cells[i+2])
					else:
						cells[i+2]=8000
				ids.append(cells[1])
			if filt=='0':
				lines.append(cells)
			elif filt=='1':
				if choice[0:1]=='<':
					if cells[int(a)+1]<float(choice[1:len(choice)]):
						## --------- 170203-- MODIFICATION ---------------------- ##
						## E.g. If -7.1 < -6.0, then keep it (we want to filter
						## all those that are higher than -6.0, i.e. -5.9, -5.8...
						## Because they show less inhibitory capacity
						counter += 1
						#print("This is cells" + "{0}".format(cells[int(a)+1]))
						#print("This is float" + "{0}".format(float(choice[1:len(choice)])))
						## Save filtered IDs
						filtered_ids.append(cells[1])
						## --------- 170203-- END OF MODIFICATION ---------------------- ##
						## Remove the ID of the PDB from the list
						ids.remove(cells[1])
						lines.append(cells)
				elif choice[0:1]=='>':
					if cells[int(a)+1]>float(choice[1:len(choice)]):
						## --------- 170203-- MODIFICATION ---------------------- ##
						## E.g. If -5.9 > -6.0, then keep it (we want to filter
						## all those that are lower than -6.0, i.e. -6.1, -7.0...
						counter += 1
						## Save filtered IDs
						filtered_ids.append(cells[1])
						## --------- 170203-- END OF MODIFICATION ---------------------- ##
						ids.remove(cells[1])
						lines.append(cells)
				
				else:
					b, f=choice.split(',')
					if cells[int(a)+1]>float(b) and cells[int(a)+1]<float(f):
						counter += 1
						## Save filtered IDs
						filtered_ids.append(cells[1])
						ids.remove(cells[1])
						lines.append(cells)
		## If it is a header, get the header line...
		else:
			title=line
			
	## How many PDBs have I filtered?
	print("This is the total of filtered pdbs: " + "{0}".format(counter))
    
    ## Order the lines by the user-chosen entry in descending order
	lines.sort(key=itemgetter(int(a)+1))
	for i in range(len(lines)):
		for j in range(18):
			if lines[i][j]==8000:
				lines[i][j]='Null'
	fil_w_txt.write(title)
	## Print the lines there in order
	for i in range(len(lines)):
		fil_w_txt.write(lines[i][0] + '\t' + lines[i][1] + '\t' + str(lines[i][2]) + '\t' + str(lines[i][3]) + '\t' + str(lines[i][4]) + '\t' + str(lines[i][5]) + '\t' + str(lines[i][6]) + '\t' + str(lines[i][7]) + '\t' + str(lines[i][8]) + '\t' + str(lines[i][9]) + '\t' + str(lines[i][10]) + '\t' + str(lines[i][11]) + '\t' + str(lines[i][12]) + '\t' + str(lines[i][13]) + '\t' + str(lines[i][14]) + '\t' + str(lines[i][15]) + '\t' + str(lines[i][16]) + '\t' + str(lines[i][17]) + '\n')
	fil_r_txt.close()
	fil_w_txt.close()
######MODIFICATION-SA-JUN-15-SAVING IN SPECIFIC DIRECTORIES REGARDING THE KIND OF FILTERING ALL THE OUTPUT FILES#########
	if filt=='0':
		#os.remove(sys.argv[1] + "output.txt")
		os.remove(sys.argv[1] + "output.tsv")
		os.rename(sys.argv[1] + "n_output.txt", sys.argv[1] + "output.tsv")
	elif filt=='1':
		#os.remove(sys.argv[1] + "output.txt")
		os.remove(sys.argv[1] + "output.tsv")
		os.rename(sys.argv[1] + "n_output.txt", sys.argv[1] + sys.argv[5]+ "/" + "filtered_output.tsv")
	## This do with everything!
	title=re.split('\t', title.strip())
	lines.insert(0,title)
	fil_w_csv=open(sys.argv[1] + "n_output.csv", 'wb')
	k=csv.writer(fil_w_csv, delimiter=',')
	k.writerows(lines)
	fil_w_csv.close()
	if filt=='0':
		os.remove(sys.argv[1] + "output.csv")
		os.rename(sys.argv[1] + "n_output.csv", sys.argv[1] + "output.csv")
		plot(open(sys.argv[1] + "output.csv", 'r'), sys.argv[5]+ "/")
	elif filt=='1':
		#os.remove(sys.argv[1] + "output.csv")
		os.rename(sys.argv[1] + "n_output.csv", sys.argv[1] + sys.argv[5] + "/" + "filtered_output.csv")
		plot(open(sys.argv[1] + sys.argv[5] + "/" + "filtered_output.csv", 'r'), sys.argv[5] + "/")

    #removes those lowest energy PDB whose entries have been removed from the output file
	#Modified 15-03-16 --> Problems with the filtering and keeping only lowest energy pdbs
	if filt=='1':
		#copy(sys.argv[1] + "lowest_energy_pdb", sys.argv[1] + sys.argv[5] + "/" + "lowest_energy_pdb_filtered")
        #for root, dirs, filenames in os.walk(sys.argv[1] + "lowest_energy_pdb"):
		#for root, dirs, filenames in os.walk(sys.argv[1] + sys.argv[5] + "/" + "lowest_energy_pdb_filtered"):
		#	for i in range(len(ids)):
		#		os.remove(os.path.join(root, ids[i] + '.pdb'))
		## --------- 170203-- MODIFICATION ---------------------- ##
		print("Copying the lowest energy pdb files in the \"lowest_energy_pdb\" directory ... ... ...")
		newdir= sys.argv[1] + sys.argv[5] + "/" + "lowest_energy_pdb_filtered/"
		if not os.path.isdir(newdir):
			os.makedirs(newdir)
		for filename in os.listdir(sys.argv[1] + "lowest_energy_pdb/"):
			for i in range(len(filtered_ids)):
				if filtered_ids[i] in filename:
					#print(ids[i])
					#print(filename)
					#os.rename(sys.argv[1] + "lowest_energy_pdb/" + "{0}".format(filename), sys.argv[1] + sys.argv[5] + "/" + "lowest_energy_pdb_filtered/" + "{0}".format(filename))
					shutil.copy(sys.argv[1] + "lowest_energy_pdb/" + "{0}".format(filename), sys.argv[1] + sys.argv[5] + "/" + "lowest_energy_pdb_filtered/" )
		## --------- 170203-- END OF MODIFICATION ---------------------- ##	
#########################################################################################################################

if __name__ == '__main__':
    a=sys.argv[2] # a = 8 (parameter to order, this is dG)
    b=sys.argv[5] # b = "filtered_results" (name of the filtered directory)
    choice=sys.argv[3] # choice = "<-6.0" (choice of filtering)
    filt=sys.argv[4] # Do you want to filter? 1--> yes, 0 --> no
    filtering(a, choice, filt)  ## Declare function to filter
