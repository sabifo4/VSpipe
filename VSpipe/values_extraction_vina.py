#!/usr/bin/env python
import sys
import csv
import re
import os
import math
import decimal
from decimal import Decimal 

#add in the output file the DG, Ki and ligand efficiency for each ligand
def values_extraction_vina():
    cnt=0
    cnt_no=0
    fil_r_txt=open(sys.argv[1] + "vina_log/log_" + sys.argv[2] + ".txt", "r")
    #extract the DG information from the log file
    for line in fil_r_txt:
        if line.startswith('---')==1:
            columns=re.split(' ', next(fil_r_txt).strip())
            columns=[x for x in columns if x]
            DG=float('%.2f' % round(float(columns[1]), 2))
            break
    fil_r_txt.close()
    #calculate the Ki value
    R=1.987*(10**(-3))
    T=298.15
    Ki=float('%.2f' % round(float(math.exp(DG/(R*T))*(10**(6))), 2))
    Kimolar = Ki*(0.000001)
    fil_r_pdbqt=open(sys.argv[1] + "vina_pdbqt/" + sys.argv[2] + "_vina.pdbqt", "r")
    #check the position of the PDBQT file where the lowest DG is
    for line in fil_r_pdbqt:
        if line.startswith('REMARK VINA RESULT:')==1:
            col_pdbqt=re.split(' ', line.strip())
            col_pdbqt=[x for x in col_pdbqt if x]
            if col_pdbqt[3]==str(DG):
                break
    #write in a PDB file the lowest energy structure from the PDBQT file
    fil_w_pdb=open(sys.argv[1] + "lowest_energy_pdb/" + sys.argv[2] +  ".pdb", "w")
    for line in fil_r_pdbqt:
        if line.startswith('ENDMDL')==1:
                break
        if line.startswith('HETATM')==1:
            #non-hydrogen atoms
            if line[11:14].strip(' ').startswith('H')==0:
                cnt+=1
            #polar atoms
            if line[11:14].strip(' ').startswith('O')==1 or line[11:14].strip(' ').startswith('N')==1:
                cnt_no+=1
            ######MODIFICATION-SA-March15####################################################
            #####It has to be added the information found in 77-78 columns in all pdb files
            #####This information is added to the fil_w_txt################################
            #Before:
            #fil_w_pdb.write(line[0:66])
            #fil_w_pdb.write("\n")
            #Now:
            str1 = line[0:66]
            str2 = (' ')*11+line[11:16].strip(' ')
            str3 = str1 + str2
            
            fil_w_pdb.write('{0}'.format(str3))
            fil_w_pdb.write("\n")
            ###############################################################################
    fil_w_pdb.close()
    fil_r_pdbqt.close()
    ligand_efficiency=float('%.2f' % round(float(DG/cnt), 2))
    ###MODIFIED-SA-March15##############
    #There is a problem with 'math', so let's use Decimal and decimal, it is the same#####
    #Before:
    #NSEI=(-math.log10(Ki))/cnt_no
    #NBEI=(-math.log10(Ki))/cnt
    #nBEI=-math.log10(Ki/cnt)
    #Now:
    NSEI=(-decimal.Decimal(float(Kimolar)).log10())/cnt_no
    NBEI=(-decimal.Decimal(float(Kimolar)).log10())/cnt
    nBEI=-decimal.Decimal(float(Kimolar)/cnt).log10()
    #add DG, Ki, ligand_efficiency, BEI, SEI, NBEI, NSEI, nBEI, mBEI in the tab delimited output file
    # 171117 - SAC - It is a tsv and not a txt
    #fil_r_txt=open(sys.argv[1] + "output.txt", "r")
    fil_r_txt=open(sys.argv[1] + "output.tsv", "r")
    fil_w_txt=open(sys.argv[1] + "n_output.txt", "w")
    for line in fil_r_txt:
        cells=re.split('\t', line.strip())
        if cells[1]==sys.argv[2]:
            if cells[2]!='Null':
            #####MODIFICATION####
                #Before
                #BEI=(-math.log10(Ki))/float(cells[2])
                #mBEI=-math.log10(Ki/float(cells[2]))
                #nOW:
                BEI=float(-decimal.Decimal(float(Kimolar)).log10())/(float(cells[2])*0.001)
                mBEI=-decimal.Decimal(float(Kimolar)/(float(cells[2])*0.001)).log10()
                
            else:
                BEI='Null'
                mBEI='Null'
            if cells[7]!='Null':
                #SEI=(-math.log10(Ki))/float(cells[7])
                SEI=float(-decimal.Decimal(Kimolar).log10())/(float(cells[7])*0.01)
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
        if cells[1]==sys.argv[2]:
            fil_w_csv.write(line.strip() + ',' + str(DG) + ',' + str(Ki) + ',' + str(ligand_efficiency) + ',' + str(BEI) + ',' + str(SEI) + ',' + str(NSEI) + ',' + str(NBEI) + ',' + str(nBEI) + ',' + str(mBEI) + '\n')
        else:
            fil_w_csv.write(line)
    fil_r_csv.close()
    fil_w_csv.close()
    os.remove(sys.argv[1] + "output.csv")
    os.rename(sys.argv[1] + "n_output.csv", sys.argv[1] + "output.csv")
    
if __name__ == '__main__':
    values_extraction_vina()
