#!/usr/bin/env python
# coding=utf-8
import sys
import csv
import re
import os

def next(iterator):
    try:
        iternext = iterator.next.__call__
    except AttributeError:
        raise TypeError("%s object is not an iterator" % type(iterator).__name__)
    try:
        return iternext()
    except StopIteration:
        return default

def datasheet_extraction(ids_zen, usr_db, usr_choice):
    fil_r_sdf=open(sys.argv[1], "r")
    # Modified by SAC - 171117: It is not a txt, it is a tsv
    #fil_w_txt=open(sys.argv[3] + "/output.txt", "w")
    fil_w_txt=open(sys.argv[3] + "/output.tsv", "w")
    in_list, outer_list, count, code, del_code=[[] for _ in range(5)]
    m=[0,0,0,0,0,0,0,0,0]
    lips=[0,0,0,0,0,0]
    in_list.extend(m)
    in_count=0
    lip_cnt=0
    flag=0
    visited=0
    flag_lip=0
    cnt_zen=0
    #if user input is "default" then RO5 is applied
    if re.search('default',usr_choice, re.IGNORECASE):
        flag_lip=1
        lips=[500, 5, 5, 10, 150, 8]
    #if user decides to edit the RO5 limitations
    elif re.search('No',usr_choice, re.IGNORECASE) is None:
        flag_lip=1
        lips=re.split('[^0-9.?]+', usr_choice)
        
    for line in fil_r_sdf:
        #check the missing data of each molecule and replace with Null in the corresponding entry
        if line.startswith('$$$$')==1:
            cnt_zen+=1
            visited=0
            if 1 not in count:
                code.append('Null')
            i=range(0,9)
            n=[x for x in i if x not in count]
            n=[x+in_count*9 for x in n]
            in_list=[i for j, i in enumerate(in_list) if j not in n]
            [in_list.insert(x, -800) for x in n]
            count=[]
            #if RO5 or edited RO5 is implemented then certain entries are written in the output
            if (in_list[in_count*9+2]<float(lips[0]) and in_list[in_count*9+4]<float(lips[1]) and in_list[in_count*9+5]<float(lips[2]) and in_list[in_count*9+6]<float(lips[3]) and in_list[in_count*9+7]<float(lips[4]) and in_list[in_count*9+8]<float(lips[5]) and flag_lip==1)  or (re.search('No',usr_choice, re.IGNORECASE)):
                for q,a in enumerate(in_list):
                    if a==-800:
                        in_list[q]='Null'
                in_count+=1
                in_list.extend(m)
            #if no RO5 or edited RO5 is applied then all entries are written in the output
            else:
                lip_cnt+=1
                del_code.append(in_list[-8])
                for w in range(9):
                    in_list.pop()
                in_list.extend(m)
        #extract canonical smiles from each ligand
        if re.search('>  <cansmi>', line, re.IGNORECASE) is not None:
            in_list.pop(in_count*9)
            in_list.insert(in_count*9, next(fil_r_sdf).strip())
            count.append(0)
        #extract code ID from each ligand
        if re.search('>  <(Code|ID(NUMBER)?|Unique_ID|InstanceId)>', line, re.IGNORECASE) is not None:
            tmp=next(fil_r_sdf).strip()
            tmp=tmp.replace(' ', '')
            tmp=tmp.replace('_', '')
            code.append(tmp)
            in_list.pop(in_count*9+1)
            in_list.insert(in_count*9+1, tmp)
            count.append(1)
        #if SDF file is from ZENOBIA or if it abides by the ZENOBIA file format then extract code ID from each ligand
        else:
            if re.search('ZENOBIA',usr_db):
                if cnt_zen<len(ids_zen):
                    code.append(ids_zen[cnt_zen])
                    in_list.pop(in_count*9+1)
                    in_list.insert(in_count*9+1, ids_zen[cnt_zen])
                    count.append(1)
                    visited=1
        #extract molecular weight from each ligand
        if re.search('>  <((M(OL)?)?W(EIGHT)?|Molecular(\s)?Weight)>', line, re.IGNORECASE) is not None and 2 not in count:
            in_list.pop(in_count*9+2)
            in_list.insert(in_count*9+2, float('%.3f' % round(float(next(fil_r_sdf).strip()), 3)))
            count.append(2)
        #extract logS from each ligand
        if re.search('>  <(cLogS|LogSw)>', line, re.IGNORECASE) is not None:
            in_list.pop(in_count*9+3)
            in_list.insert(in_count*9+3, float('%.3f' % round(float(next(fil_r_sdf).strip()), 3)))
            count.append(3)
        #extract logP from each ligand
        if re.search('>  <C?_?Log_?P>', line, re.IGNORECASE) is not None and 4 not in count:
            in_list.pop(in_count*9+4)
            in_list.insert(in_count*9+4, float('%.3f' % round(float(next(fil_r_sdf).strip()), 3)))
            count.append(4)
        #extract hydrogen bond donors from each ligand
        if re.search('>  <(HBD|H_?b?(ond)?_?don(ors)?)>', line, re.IGNORECASE) is not None and 5 not in count:
            in_list.pop(in_count*9+5)
            in_list.insert(in_count*9+5, float('%.3f' % round(float(next(fil_r_sdf).strip()), 3)))
            count.append(5)
        #extract hydrogen bond acceptors from each ligand
        if re.search('>  <(HBA2?|H_?b?(ond)?_?acc(eptors)?)>', line, re.IGNORECASE) is not None and 6 not in count:
            in_list.pop(in_count*9+6)
            in_list.insert(in_count*9+6, float('%.3f' % round(float(next(fil_r_sdf).strip()), 3)))
            count.append(6)
        #extract tPSA from each ligand
        if re.search('>  <t?PSA>', line, re.IGNORECASE) is not None and 7 not in count:
            in_list.pop(in_count*9+7)
            in_list.insert(in_count*9+7, float('%.3f' % round(float(next(fil_r_sdf).strip()), 3)))
            count.append(7)
        #extract rotatable bonds from each ligand
        if re.search('>  <R(otat(able|ing)_)?B(onds)?>', line, re.IGNORECASE) is not None:
            in_list.pop(in_count*9+8)
            in_list.insert(in_count*9+8, float('%.3f' % round(float(next(fil_r_sdf).strip()), 3)))
            count.append(8)
    for w in range(9):
        in_list.pop()
    k=0
    #tab delimited output file
    fil_w_txt.write('Smiles' + '\t' + 'CodeID' + '\t' + 'MolecularWeight' + '\t' + 'cLogS' + '\t' + 'cLogP' + '\t' + 'HBD' + '\t' + 'HBA' + '\t' + 'PSA' + '\t' + 'ROTATABLE_BONDS' + '\t' + 'DG' + '\t' + 'Ki' + '\t' + 'LIGAND_EFFICIENCY' + '\t' + 'BEI' + '\t' + 'SEI' + '\t' + 'NSEI' + '\t' + 'NBEI' + '\t' + 'nBEI' + '\t' + 'mBEI' + '\n')
    title=['Smiles', 'CodeID', 'MolecularWeight', 'cLogS', 'cLogP', 'HBD', 'HBA', 'PSA', 'ROTATABLE_BONDS', 'DG', 'Ki', 'LIGAND_EFFICIENCY', 'BEI', 'SEI', 'NSEI', 'NBEI', 'nBEI', 'mBEI']
    outer_list.append(title)
    for i in range(0,len(in_list),9):
        out_list=[]
        fil_w_txt.write(in_list[i] + '\t' + str(in_list[i+1]) + '\t' + str(in_list[i+2]) + '\t' + str(in_list[i+3]) + '\t' + str(in_list[i+4]) + '\t' + str(in_list[i+5]) + '\t' + str(in_list[i+6]) + '\t' + str(in_list[i+7]) + '\t' + str(in_list[i+8]) + '\n')
        for j in range(9):
            out_list.append(in_list[i+j])
        outer_list.append(out_list)
        k+=1
    fil_w_csv=open(sys.argv[3] + '/output.csv', 'wb')
    a=csv.writer(fil_w_csv, delimiter=',')
    a.writerows(outer_list)
    fil_r_sdf.close()
    fil_w_txt.close()
    fil_w_csv.close()
    return (code, del_code)

#delete those PDBQT files that do not abide by RO5, if this option is applied
def pdbqts_delete(del_code):
    for root, dirs, filenames in os.walk(sys.argv[3] + '/pdbqt_lip_rules'):
        for i in range(len(del_code)):
            os.remove(os.path.join(root, del_code[i] + '.pdbqt'))

#check if the SDF file abides by ZENOBIA's file format
def zenobia_type():
    fil_r_sdf=open(sys.argv[1], "r")
    cnt_zen=0
    for line in fil_r_sdf:
        if line.startswith('$$$$'):
            cnt_zen+=1
    fil_r_sdf.close()
    fil_r_sdf=open(sys.argv[1], "r")
    ids_zen=[]
    first_id=fil_r_sdf.readline().strip()
    if re.search('^[A-Za-z0-9]+$', first_id) is not None:
        ids_zen.append(first_id)
        for line in fil_r_sdf:
            if line.startswith('$$$$'):
                cnt_zen-=1
                if cnt_zen!=0:
                    second_id=next(fil_r_sdf).strip()
                    ids_zen.append(second_id)
    else:
        ids_zen.append("")
    fil_r_sdf.close()
    if ids_zen[0]!="":
        usr_db='ZENOBIA'
    else:
        usr_db='none'
    return (ids_zen, usr_db)

if __name__ == '__main__':
    if sys.argv[4]=='3':
        [ids_zen, usr_db]=zenobia_type()
    else:
        ids_zen=''
        usr_db='none'
    usr_choice=sys.argv[2]
    [code, del_code]=datasheet_extraction(ids_zen, usr_db, usr_choice)
    if del_code:
        pdbqts_delete(del_code)
