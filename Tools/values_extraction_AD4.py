#!/usr/bin/env python
import sys
import csv
import re
import os
import math
import decimal
from decimal import Decimal

#add in the output file the DG, Ki and ligand efficiency for each ligand
#sys.argv[1] = results_directory
#sys.argv[2] = filename (the name of the ligand)
def values_extraction_AD4():
    cnt=0
    cnt_no=0
    fil_r_txt=open(sys.argv[1] + "summary/summary_" + sys.argv[2] + ".txt", "r")
    for line in fil_r_txt:
        if line.startswith('lowestEnergy')==0:
            columns=re.split(',', line.strip())
            columns=[x.strip(' ') for x in columns]
    a, b=os.path.split(columns[0])
    filename=b #lowestEnergy??
    
    #extract the DG information from the summary file
    DG=float('%.2f' % round(float(columns[4]), 2)) #%.2f gets just the two first decimals of "round(float(columns[4]),2))"
						   #round(x, y) --> y is the number of decimals (2) of x (what is in column 4)
    ligand_efficiency=columns[9]
    fil_r_txt.close()
    
    #fil_r_txt now is the '.dlg' file and not the '.txt' file saved in summary
    fil_r_txt=open(sys.argv[1] + "dlg/" + sys.argv[2] + "/" + sys.argv[2] + ".dlg", "r")
    visited=0
    #calculate the Ki always in micromolar
    R=1.987*(10**(-3))
    T=298.15
    Ki=float('%.2f' % round(float(math.exp(DG/(R*T))*(10**(6))), 2))
    Kimolar = Ki*(0.000001)
    for line in fil_r_txt:
        #check the position of the DLG file where the lowest DG is
        if re.search('USER\s+Estimated Free Energy of Binding\s+=\s+' + str(DG), line) and visited==0:
            if line[0:6]=='DOCKED':
                continue
            visited=1
            tmp=next(fil_r_txt).strip()
            break
    #write in a PDB file the lowest energy structure from the DLG file
    fil_w_txt=open(sys.argv[1] + "lowest_energy_pdb/" + sys.argv[2] + ".pdb", "w")
    for line in fil_r_txt:
        if line.startswith('TER')==1:
                break
        if line.startswith('ATOM')==1:
            #non-hydrogen atoms
            if line[11:16].strip(' ').startswith('H')==0:
                cnt+=1
            #polar atoms
            if line[11:16].strip(' ').startswith('O')==1 or line[11:14].strip(' ').startswith('N')==1:
                cnt_no+=1
            ######MODIFICATION-SA-Feb15####################################################
            #####It has to be added the information found in 77-78 columns in all pdb files
            #####This information is added to the fil_w_txt################################
            #Before:
            #fil_w_txt.write(line[0:54])
            #fil_w_txt.write("\n")
            #Now:
            str1 = line[0:54]
            str2 = (' ')*23+line[11:14].strip(' ') #MODIFICATION-SA-Apr15-TRYING TO GET ONLY
	    ###THE LETTER OF THE ATOM ALONE, NOT OTHER LETTERS#############################
            str3 = str1 + str2
            
            fil_w_txt.write('{0}'.format(str3))
            fil_w_txt.write("\n")
    #print cnt
    fil_r_txt.close()
    fil_w_txt.close()
    ###MODIFIED-SA-Apr15##############
    #Before:
    #NSEI=(-math.log10(float(Kimolar)))/cnt_no
    #NBEI=(-math.log10(float(Kimolar)))/cnt
    #nBEI=-math.log10(float(Kimolar)/cnt)
    NSEI=(-decimal.Decimal(float(Kimolar)).log10())/cnt_no
    NBEI=(-decimal.Decimal(float(Kimolar)).log10())/cnt
    nBEI=-decimal.Decimal(float(Kimolar)/cnt).log10()
    #add DG, Ki, ligand_efficiency, BEI, SEI, NBEI, NSEI, nBEI, mBEI in the tab delimited output file
    # 171117- SAV- It is a tsc and not a txt
    #fil_r_txt=open(sys.argv[1] + "output.txt", "r")
    fil_r_txt=open(sys.argv[1] + "output.tsv", "r")
    fil_w_txt=open(sys.argv[1] + "n_output.txt", "w")
    for line in fil_r_txt:
        cells=re.split('\t', line.strip())
        if cells[1]==filename:
            if cells[2]!='Null':
		###MODIFICATION-SA-Apr15###################
		#Before:
                #BEI=(-math.log10(float(Kimolar)))/(float(cells[2])*0.001)
                #mBEI=-math.log10(float(Kimolar)/(float(cells[2])*0.001))
		BEI=float(-decimal.Decimal(float(Kimolar)).log10())/(float(cells[2])*0.001)
                mBEI=-decimal.Decimal((float(Kimolar))/(float(cells[2])*0.001)).log10()
            else:
                BEI='Null'
                mBEI='Null'
            if cells[7]!='Null':
		###MODIFICATION-SA-Apr15##################
		##Before:
                #SEI=(-math.log10(float(Kimolar)))/(float(cells[7])*0.01)
		SEI=float(-decimal.Decimal(float(Kimolar)).log10())/(float(cells[7])*0.01)
            else:
                SEI='Null'
            fil_w_txt.write(line.strip() + '\t' + str(DG) + '\t' + str(Ki) + '\t' + str(ligand_efficiency) + '\t' + str(BEI) + '\t' + str(SEI) + '\t' + str(NSEI) + '\t' + str(NBEI) + '\t' + str(nBEI) + '\t' + str(mBEI) + '\n')
        else:
            fil_w_txt.write(line)
    fil_r_txt.close()
    fil_w_txt.close()
    #os.remove(sys.argv[1] + "output.txt")
    os.remove(sys.argv[1] + "output.tsv")
    #os.rename(sys.argv[1] + "n_output.txt", sys.argv[1] + "output.txt")
    os.rename(sys.argv[1] + "n_output.txt", sys.argv[1] + "output.tsv")
    #add DG, Ki, ligand_effieciency, BEI, SEI, NBEI, NSEI, nBEI, mBEI in the comma delimited output file
    fil_r_csv=open(sys.argv[1] + "output.csv", "r")
    fil_w_csv=open(sys.argv[1] + "n_output.csv", "w")
    for line in fil_r_csv:
        cells=re.split(',', line.strip())
        if cells[1]==filename:
            fil_w_csv.write(line.strip() + ',' + str(DG) + ',' + str(Ki) + ',' + str(ligand_efficiency) + ',' + str(BEI) + ',' + str(SEI) + ',' + str(NSEI) + ',' + str(NBEI) + ',' + str(nBEI) + ',' + str(mBEI) + '\n')
        else:
            fil_w_csv.write(line)
    fil_r_csv.close()
    fil_w_csv.close()
    os.remove(sys.argv[1] + "output.csv")
    os.rename(sys.argv[1] + "n_output.csv", sys.argv[1] + "output.csv")
    
if __name__ == '__main__':
    values_extraction_AD4()
