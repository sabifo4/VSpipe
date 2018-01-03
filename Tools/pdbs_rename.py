import sys
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

#check the code ID of each ligand in the SDF file
def check_code(ids_zen, usr_db):
    code=[]
    fil_r_sdf=open(sys.argv[1], "r")
    cnt_zen=0
    visited=0
    for line in fil_r_sdf:
        if line.startswith('$$$$')==1:
            cnt_zen+=1
            if count!=1:
                code.append("Null")
            visited=0
        if re.search('>  <(Code|ID(NUMBER)?|Unique_ID|InstanceId)>', line, re.IGNORECASE) is not None:
            tmp=next(fil_r_sdf).strip()
            code.append(tmp)
            count=1
        elif re.search('ZENOBIA',usr_db) and visited==0:
            if cnt_zen<len(ids_zen):
                code.append(ids_zen[cnt_zen])
                count=1
                visited=1
    fil_r_sdf.close()
    return code

#rename the PDB files after their code ID and put the code
#ID inside the file where the COMPOUND string is given
def pdbs_rename(code):
    cnt=0
    for root, dirs, filenames in os.walk(sys.argv[2]):
        while filenames:
            for filename in filenames:
                if re.match('^ligand' + str(cnt+1) + '.pdb$', filename) is not None:
                    filename_old=os.path.join(root, filename)
                    filename_new=os.path.join(root, code[cnt] + '.pdb')
                    os.rename(filename_old, filename_new)
                    cnt+=1
                    filenames.remove(filename)
                    break
                
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
    if sys.argv[3]=='3':
        [ids_zen, usr_db]=zenobia_type()
    else:
        ids_zen=''
        usr_db='none'
    code=check_code(ids_zen, usr_db)
    #replace every gap in the code ID with underscore
    code=[x.replace(' ', '') for x in code]
    code=[x.replace('_', '') for x in code]
    pdbs_rename(code)
