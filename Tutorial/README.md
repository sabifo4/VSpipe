## __Download VSpipe local__

First of all, you should clone this repository in your local PC. You can download it 
by clicking either the `Clone or download` button in the Git repository or [here](https://github.com/sabifo4/VSpipe/archive/master.zip).
If you have `git` installed, you can also create a directory in your local PC to where you
want to save it, and type the following in a terminal:

```bash
git clone https://github.com/sabifo4/VSpipe
```

This repository consists of the following:

```  
Applications
  |- VSpipe-master 
      |- .git 
      |- Installation 
      |     |- Install_dependencies_MacOSX.md 
      |     |- Install_dependencies_Linux.md 
      |     |- Install_dependencies_WLS.md 
      |
      |- Tutorial 
      |     |- *.md
      | 
      |- README.md  
```

Once you have cloned this repository, you can find the the latest release version of `VSpipe` [here](https://github.com/sabifo4/VSpipe/releases/tag/v1.0), which can 
also be found if you go to the `release` tab in the GitHub repository. 
Once you have downloaded the `VSpipe.tar.gz` file, please untar it and save it, for instance, inside this GitHub repository or 
in your preferred location. If you saved the GitHub repository under the `~/Applications` directory and the `VSpipe.tar.gz` inside 
the cloned repository, you should have something like this once you have untarred `VSpipe.tar.gz` file: 

```  
Applications
  |- VSpipe-master 
      |- .git 
      |- Installation 
      |     |- Install_dependencies_MacOSX.md 
      |     |- Install_dependencies_Linux.md 
      |     |- Install_dependencies_WLS.md 
      | 
      |- Tutorial 
      |     |- *.md
      | 
      |- VSpipe
      |     |- Tools 
      | 
      |- README.md	  
```

After that, please follow the installation instructions for your operating system to install the third-party 
tools `VSpipe` relies on:   

   1. Installation for Linux *- only tested on Ubuntu but should work for any Linux distribution*: click [here](https://github.com/sabifo4/VSpipe/blob/master/Installation/Install_dependencies_Ubuntu.md).   
   2. Installation for the Windows Linux Subsystem *- only tested on Ubuntu but should work for any Linux distribution*: click [here](https://github.com/sabifo4/VSpipe/blob/master/Installation/Install_dependencies_WLS.md)   
   3. Installation for Mac OS X: click [here](https://github.com/sabifo4/VSpipe/blob/master/Installation/Install_dependencies_MacOSX.md)   
   
If you have followed the steps described in the installation file, you might have an alias to run 
`VSpipe` on the terminal just by typing `VSpipe` on the terminal. If you have already typed `VSpipe` on 
your terminal and you see this message...  

```
|-------------------------------------------------------------------|
|                        VSpipe v1.0                                |
|-------------------------------------------------------------------|
| Pipeline designed and developed by:                               |
| Sandra Alvarez-Carretero, Niki Pavlopoulou,                       |
| Jane Gilsenan, and Lydia Tabernero                                |
|                                                                   |
| Pipeline currently maintained by:                                 |
| Sandra Alvarez-Carretero                                          |
|                                                                   |
| If you use VSpipe to carry out yor VSs, please cite:              |
|    Alvarez-Carretero, et al. (2018) Molecules, 23(2), 353         |
|                 https://doi.org/10.3390/molecules23020353         |
|                                                                   |
| You can find a tutorial and the manual for VSpipe here:           |
|    https://github.com/sabifo4/VSpipe                              |
|                                                                   |
| If you have further questions or need to report a bug, please     |
| send a message to:                                                |
|    vspipe.local@gmail.com                                         |
|                                                                   |
|                     Happy Docking! :)                             |
|-------------------------------------------------------------------|


#------------------------#
#  RECEPTOR PREARATION   #
#------------------------#

If you have already prepared your receptor,
which means that you must have a directory, for instance called
"receptor", with the following content

   receptor
        |- XXX.pdb
        |- XXX_clean.pdb
        |- XXX.pdbqt
        |- sample.gpf

then you can also reuse your prepared receptor.
Please type "yes" if you want to reuse your receptor. Otherwise,
please type "no" and then press [ENTER]:

```

... then you can already run `VSpipe`. Otherwise, you might have missed an important step 
during the installation of the third-party tools.


## __Run VSpipe local__

### 1. Set the working directory

First of all, set your working directory. Open a terminal in your preferred location and 
create your working directory. In this tutorial, the working directory is going to be called `test_VSpipe`,
although you can change this name if you want to. Note that this will not change the next steps in the tutorial.
The path to `test_VSpipe` for this tutorial example is `/home/user/my_dockings/test_VSpipe`, hence:

```bash
$ pwd
/home/user/my_dockings
$ mkdir test_VSpipe
$ cd test_VSpipe 
$ pwd
/home/user/my_dockings/test_VSpipe
```

### 2. Run a virtual screening with VSpipe
Once you are inside your working directory, you are ready to run `VSpipe`. If you have followed the installation 
procedure, you might jus be able to run `VSpipe` by typing `VSpipe` on the terminal. Otherwise, you will need 
to type the whole path to the bash script:

First, make sure you are in your working directory

```bash
pwd 
/home/user/my_dockings/test_VSpipe
```

Then, you can run `VSpipe` for the first time saving a log file 

```bash
VSpipe 2>&1 | tee logfile.txt
```

If you want a log file saving the messages printed on the screen, you should run `VSpipe` as:

```bash
VSpipe 2>&1 | tee logfile.txt
```

This will create a file called `logfile.txt` in your working directory (`/home/user/my_dockings/test_VSpipe`).
Once `VSpipe` is running - with or without creating a log file - you will see this message:

```
|-------------------------------------------------------------------|
|                        VSpipe v1.0                                |
|-------------------------------------------------------------------|
| Pipeline designed and developed by:                               |
| Sandra Alvarez-Carretero, Niki Pavlopoulou,                       |
| Jane Gilsenan, and Lydia Tabernero                                |
|                                                                   |
| Pipeline currently maintained by:                                 |
| Sandra Alvarez-Carretero                                          |
|                                                                   |
| If you use VSpipe to carry out yor VSs, please cite:              |
|    Alvarez-Carretero, et al. (2018) Molecules, 23(2), 353         |
|                 https://doi.org/10.3390/molecules23020353         |
|                                                                   |
| You can find a tutorial and the manual for VSpipe here:           |
|    https://github.com/sabifo4/VSpipe                              |
|                                                                   |
| If you have further questions or need to report a bug, please     |
| send a message to:                                                |
|    vspipe.local@gmail.com                                         |
|                                                                   |
|                     Happy Docking! :)                             |
|-------------------------------------------------------------------|


#------------------------#
#  RECEPTOR PREARATION   #
#------------------------#

If you have already prepared your receptor,
which means that you must have a directory, for instance called
"receptor", with the following content

   receptor
        |- XXX.pdb
        |- XXX_clean.pdb
        |- XXX.pdbqt
        |- sample.gpf

then you can also reuse your prepared receptor.
Please type "yes" if you want to reuse your receptor. Otherwise,
please type "no" and then press [ENTER]:
```

This step asks you if you want to reuse your receptor. If you have not run 
VSpipe before, please type `no` as you need to prepare the PDB file with your 
target protein before the docking starts. After typing `no` and pressing `ENTER` (RETURN key), you are asked the following 
questions: 

```
Please type a name for the directory where all the files concerning
the receptor will be. After that, please press [ENTER]:
receptor

Please type the name of the PDB file for the receptor and upload
it in the directory receptor. After that, please press
[ENTER]:
3X4P.pdb

Please use ADT to manually create your "gpf" file, in which you
will define the grid box. Then, please manually save the file as
"sample.gpf" under the directory receptor.
Once this is done, please press [ENTER]:

```

In this snippet, we assume that you call the directory to prepare the receptor **`receptor`** and that the file 
with your target protein is **`3X4P.pdb`**. In order to generate the grid parameter file, which `VSpipe` valls `sample.gpf`, 
you should follow the [ADT tutorial](http://autodock.scripps.edu/faqs-help/tutorial/using-autodock-4-with-autodocktools/2012_ADTtut.pdf) (page 12, 
"AD4 Exercise Five: Preparing the AutoGrid Parameter File"). This is a manual task the user 
needs to carry out because it requires some knowledge about the area of the target receptor (the "grid box") where
the ligands will be later docked. Here you have an example of how this grid parameter looks like:

```
npts 40 40 40
gridfld 3X4P.maps.fld
spacing 0.375
receptor_types A C AO N AS HD
ligand_types A C HD N NA OA SA F Cl I
receptor 3X4P.pdbqt
gridcenter -21.742 19.446 -16.879
smooth 0.5
map 3X4P.A.map
map 3X4P.C.map
map 3X4P.HD.map
map 3X4P.N.map
map 3X4P.NA.map
map 3X4P.OA.map
map 3X4P.SA.map
map 3X4P.F.map
map 3X4P.Cl.map
map 3X4P.I.map
elecmap 3X4P.e.map
dsolvmap 3X4P.d.map
dielectric -0.1465
```

Note that once you have created your grid parameter file and saved it as `sample.gpf`, you should upload it 
to your `receptor` directory and press `[ENTER]`. After that, you will see this message: 

```
Please select if you want to extract only the first chain from the
3X4P.pdb, if you do not want to extract it, or if want to keep
the metal ion of your protein if it is a metalloproteinase.
If you choose not to extract the chain, then please make
sure the file is in the correct PDB format.

Please type "1", "2", or "X" (without quotation marks)
according to the option you choose:

1)Extracting the first chain without keeping the metal ion
2)Not extracting the first chain (keep the file by default)
X)Extracting the first chain and keeping the metal ion, where X is
  the name of the metal ion you want to keep. Be sure you type it
  in capital letters and in the PDB format (i.e., ZN, P, FE...)


After that, please press [ENTER]:
1
```

Let's suppose that this protein is not a metalloproteinase, so I just want to extract 
the first chain. You should not use option `2` unless you are sure that the pdb file you are using 
contains the information needed to generate a `pdbqt` file. We always recommend to use option `1` unless 
you have a metalloproteinase, in which case you should type the name of the metal ion (e.g., `FE`).

Once you enter your decision, the `pdbqt` will be generated and you will see the following messages 
printed out in your screen: 

```
Extracting the first chain from the receptor's pdb file and saving
it as receptor/3O4U_clean.pdb.

Removing water residues.
Adding hydrogens in the receptor's pdb file.
Merging charges and removing non-polar hydrogens.
Saving the receptor as receptor/3O4U.pdbqt.

adding gasteiger charges to peptide


If you chose to keep the metal ion, now set its charge to
modify the receptor/3O4U.pdbqt file. Type the charge
in this way: '+X.YZW' or '-X.YWZ' (e.g. +2.000). After that,
please press [ENTER]. If you did not keep a metal ion,
then type 'no' and, after that, please press [ENTER]:
no 
```

As we do not have a metalloproteinase, we just type `no` and press `[ENTER]`. Then, some final 
corrections will take place in the `pdbqt` file so it has the correct format. 
After that, the first step, receptor preparation, will have finished. 

```
Correcting the receptor/3O4U.pdbqt file in case it has errors.
Correcting the sample.gpf.

#------------------------#
#  LIGAND/S PREPARATION  #
#------------------------#

If you have already prepared the ligands you want to use,
please type "yes" and then press [ENTER].
Otherwise, if you need to prepare your ligands, please type
"no" and then press [ENTER]:
no
```

Now, the next step takes place: ligand/s preparation. For this quick tutorial, let's assume 
that we want to use one of the libraries already provided by `VSpipe`. Therefore, we say `no` 
and press `[ENTER]` to answer the next questions to filter and minimise this ligand library.

```
Please type a name for the directory where the files
concerning the ligands will be. After that, please
press [ENTER]:
ligands

Please upload in the ligands directory the PDB or MOL or MOL2
or SMI or CAN or SDF file/files for the ligand and, after that, please press
[ENTER]. However, if you do not want to upload your own files and you want
to use any of the ligand SDF files from public databases provided by VSpipe, please
type the corresponding number from one of the following
options:
1) AnalytiConDiscoveryNP.sdf
2) ASINEX_BB_v123_SD.sdf
3) ASINEXSynergy_Fragments.sdf
4) Chem-diverset.sdf
5) Chem-Fragment.sdf
6) Chem-MW-Set-1.sdf
7) ENAMINEBuilding_Blocks_reduced_price.sdf
8) ENAMINEfragment_library.sdf
9) IBScreenNP.sdf
10) IndofineNaturalProducts.sdf
11) Maybridge-Building_Blocks_GBP.sdf
12) Maybridge-Fragment_Collection.sdf
13) Maybridge_Pre-Fragment-COCl_PFP.sdf
14) Maybridge_Pre-Fragment-NCO.sdf
15) Maybridge_Pre-Fragment-SO2Cl.sdf
16) Maybridge_Ro3_1000_Fragment_Library.sdf
17) Maybridge_Ro3_500_Fragment_Library.sdf
18) PrincetonNP.sdf
19) SpecsNaturalProducts.sdf
20) ZENOBIA_352fragments.sdf
21) PTP_database.sdf
and then please press [ENTER].
E.g. If you want to use the Chem-diverset.sdf library, you should type "1"
14

You have chosen to use the Maybridge_Pre-Fragment-NCO.sdf file.



Producing canonical smiles and missing properties of the ~/Applications/VSpipe-master/VSpipe/Tools/database_libraries/Maybridge_Pre-Fragment-NCO.sdf file and saving it as
ligands/sdf/properties_ligands.sdf.
98 molecules converted


Deleting from the ligands/sdf/properties_ligands.sdf
the atoms that are not recognised by Autodock and saving it as
ligands/sdf/del_atoms_properties_ligands.sdf.

Your version of OpenBabel is:
Open Babel 2.4.90 -- Apr 9 2019 -- 11:56:59

Do you want to use OpenBabel to minimise your PDB structures?
If you type "no", this means that you have already taken care
of the ligand minimisation before. If you type "yes", OpenBabel
will be used to generate 3D conformers until finding the structure
with the lowest energy. Then, please press [ENTER]
no
```

In this case, we have decided to create a directory called `ligands` to save the filtered ligands from the `Maybridge_Pre-Fragment-NCO` library 
already provided by `VSpipe`. This library is identified by number `14`, this is why we have typed `14`.

After that, missing properties are added to the ligands in the selected library (information later used for the summary statistics) and you are reminded 
of the Open Babel version installed on your PC. If your library has not been minimised and you want to use Open Babel to minimise it, then type `yes`. 
During our tests, we have had some problems when minimising some libraries with newer versions of Open Babel, so you can also have your own 
minimised libraries and then skip that procedure.
For that example, we will assume that we do not want to minimise our library, so only 3D coordinates will be added, so we type `no`.
This library has 98 compounds, so you might be waiting a bit until this step has concluded to generate the `pdbqt` files for your ligands. 

```
Converting molecules in "del_atoms_properties_ligands.sdf" to pdb
and adding 3D coordinates ... ...
98 molecules converted
98 files output. The first is ligands/pdb/ligand1.pdb


Renaming the ligands/pdb/ligand#.pdb after their IDs.
Adding hydrogens in the ligands/pdb/ID#.pdb files.
Merging charges and removing non-polar hydrogens.
Saving the ligands as ligands/pdbqt/ID#.pdbqt ... ...

Please choose whether you want to apply Lipinski rules or not. If not,
please type "no". Otherwhise, please type either "default" to choose
MW<500, logP<5, HBD<5, HBA<10, TPSA<150, ROT_BONDS<8 or edit the values
that correspond to each property.
E.g. You can type "550,5.3,4,11,140,7" if you wanted to set
MW<550, logP<5.3, HBD<4, HBA<11, TPSA<140, ROT_BONDS<7.
Please take into account that, if you edit the numbers, no spaces among
them should be typed.
After that, please press [ENTER]:
no
```

Once the `pdbqt` files have been generated for the ligand library, then we are asked if we want to apply Lipinski rules. 
We will say we do not want to use them so we type `no` and press `[ENTER]`. Then, we will be asked about using either `Vina` or `AutoDock` 
to carry out virtual screenings. We will pick `Vina` and we will select a `blind` docking - Note that blind dockings should be only 
run with `Vina`, not with `AutoDock`.

```
Please choose whether you want to run Autodock4.2 or Vina.
Please type "AD4" for Autodock4.2 or "Vina" for Autodock
Vina. After that, please press [ENTER]:
vina


Please type a name for your results directory. Afer that, please
press [ENTER]:
results


Creating a datasheet that contains all the properties and the
canonical smiles of each ligand and saving it as Vina/output.csv
and Vina/output.tsv.

#----------------#
#  DOCKING STEP  #
#----------------#

Do you want to run Vina for a blind or a targeted docking?
Please, type "blind" if you want to carry out a blind docking
and "target" if you want to carry out a targeted docking.
After that, please press [ENTER]
blind
```

We are going to create a directory called `results` and then we will type `blind` when asked about the type of virtual screening to perform.
After you press `[ENTER]`, the VS will take place. You will see a message like this one for each ligand that you are going to evaluate 
during the docking step:

```
Molecule AC17031 | Running blind docking with Vina ... ...

#################################################################
# If you used AutoDock Vina in your work, please cite:          #
#                                                               #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
# Please see http://vina.scripps.edu for more information.      #
#################################################################

WARNING: The search space volume > 27000 Angstrom^3 (See FAQ)
Detected 12 CPUs
WARNING: at low exhaustiveness, it may be impossible to utilize all CPUs
Reading input ... done.
Setting up the scoring function ... done.
Analyzing the binding site ... done.
Using random seed: 2065711188
Performing search ...
0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
```

At the end of the docking, you will see the following on your screen:

```
Refining results ... done.

mode |   affinity | dist from best mode
     | (kcal/mol) | rmsd l.b.| rmsd u.b.
-----+------------+----------+----------
   1         -5.1      0.000      0.000
   2         -4.9      2.013      2.232
   3         -4.8      3.573      4.656
   4         -4.7      4.115      5.398
   5         -4.6     27.732     28.085
   6         -4.5     30.763     31.549
   7         -4.5     25.530     25.971
   8         -4.3     31.275     32.113
   9         -4.3     30.668     31.442
Writing output ... done.

#-------------------------------#
#  SUMMARISING RESULTS ... ...  #
#-------------------------------#
1 molecule converted
1 molecules converted 
```

Note that not all compounds might have passed all filters during the dockng step, hence you might see messages like the one 
generated in this example during the "summarising results" step:

```
==============================
*** Open Babel Warning  in PerceiveBondOrders
  Failed to kekulize aromatic bonds in OBMol::PerceiveBondOrders (title is Vina/lowest_energy_pdb/CC50806.pdb)

```

If this is the case, you might want to take a closer look at this compound if it was of interest in your analysis.
Note that you will see as many `1 molecule converted` messages as ligands you have used. After that, the compounds will be ordered according to increasing dG, and several plots and output files will be generated. 

```
Ordering the Vina/output.csv and
Vina/output.tsv by DG in descending order.


#-------------------------------------------------------#
#              Running R ...                            #
#-------------------------------------------------------#

You have not applied any filters. By default, the
output file has been ordered according to increasing dG
null device
          1

#-------------------------------------------------------#
#     Plots and output files have been generated !      #
#-------------------------------------------------------#



VSpipe has finished to filter the results of the virtual screening.

THANK YOU FOR USING VSpipe !!

```

This is it!! :) You can now use the output files generated and the graphs to evaluate the performance of the virtual screenings. Furthermore, you can use the R script `filtering.R` to further filter your results with more or less stringent thresholds and according to other parameters. The next section will explain how you can do this.


## __Filtering step in VSpipe__

### A.  When VSpipe runs `filtering.R` ...

By default, when you run VSpipe there is no filtering. Therefore, you will see that you get 
inside your `results` directory the following files:

```
clogP-NumComp.pdf
MW-numComp.pdf 
NSEI-NBEI.pdf
NumHBA-NumComp.pdf 
ordered_output.csv 
ordered_output.tsv 
ordered_output_ATLAS.txt 
output.csv 
output.tsv 
PSA-numComp.pdf 
SEI-BEI.pdf
```

#### What are the output files?

##### PDF files 
The `*.pdf` files are the plots that are automatically generated. 
They will use the information of **ALL** the compounds you have tested - not filtered yet !

##### OUTPUT files   

1. The `output.csv` and `output.tsv` contain the same information, they just differ in the separator.
Remember that `csv` files are "comma" separated, while `tsv` files are "tab" separated. Note that 
these two files have **NOT** been filtered yet, hence they are not ordered.
2. The `ordered_output.csv` and the `ordered_output.tsv` contain the same information, they just 
differ in the separator (see above for details). These files have *NOT* been filtered but they *DO HAVE*
been ordered according to the dG. This is the default ordering that takes place when the pipeline runs. 
3. The `ordered_output_ATLAS.txt` is written in a format that can be read by the ATLAS platform. You 
can just grab this file, plug it in ATLAS, and play around :) 

### B. When you run `filtering.R` ...

Once `VSpipe` has finished, you can call the `filtering.R` (which also lies within `VSpipe/Tools`. If you have followed previous examples, you 
might find this in the absolute path `~/Applications/VSpipe-master/VSpipe/Tools`) to further filter your analyses.

The way you call this file from a terminal is the following:

```
Rscript <path_to_VSpipe>/VSpipe/Tools/filtering.R <path_to_your_results_dir_where_you_run_VSpipe> <ORDER_PAR> <CHOICE_PAR> <FILT_PAR> <path_to_directory_where_you_want_filtered_results>
```

Let's see what each bit of this command does:

---------------------------------------

   1) _**Rscript**_: This is the command that runs R. The first argument is the `R` script and then you can have the arguments.   
   2) _**<path_to_VSpipe>/VSpipe/Tools/filtering.R**_: This is the first argument the `Rscript` commands needs: the path to the `filgering.R` file.   
   3) _**<path_to_your_results_dir_where_you_run_VSpipe>**_: This is the first argument that the `filtering.R` takes and the second `Rscript` takes. 
   The arguments is the path to the `results` directory that was created by VSpipe during 
   the virtual screening and where all the results are. If you have moved to this directory, then you can just type `results/`, **WITH THE SLASH** !!
   If you are running this command somewhere else, make sure that you type the whole path to where this `results` directory is.   
   4) _**<ORDER_PAR>**_: This is the second argument the `filtering.R` takes and the third that `Rstudio` takes: This is a number that is used to let this
   script know which column contains the property that needs to be used to order and filter the `output.csv` file. Depending on which property you want to use to 
   filter the `output.csv` file, you should type one of the following numbers:   

               1: Molecular Weight    9:  Ki
               2: cLogS               10: ligand efficiency
               3: cLogP               11: BEI
               4: HBD                 12: SEI
               5: HBA                 13: NSEI
               6: PSA                 14: NBEI
               7: rotatable bonds     15: nBEI
               8: dG                  16: mBEI 		   
   For instance, if you were to use the Ki to filter your `output.csv`, you should type a **9** as the third argument in the whole command (_**NO QUOTATION MARKS!**_).   
   5) _**<CHOICE_PAR>**_: This is the third argument the `filtering.R` takes and the fourth that `Rstudio` takes. You can filter something by a value greater or lower than 
another or withing a range. For instance:
			
			Filter molecules which Ki is larger than -5.7: ">-5.7"          # Use the symbol > followed by the value 
			Filter molecules which Ki is lower than -5.7: "<-5.7"           # Use the symbol < followed by the value 
			Filter molecules which Ki is between -3.5 and -5.7: "-5.7,-3.7" # Use a comma to separate the two values   
   Note that the quotation marks **ARE REQUIRED** !   
   6) _**<FILT_PAR>**_: This is the fourth argument the `filtering.R` takes and the fifth that `Rstudio` takes. It is **0** if you do not want to filter anything - this is the default mode the pipeline runs, in which nothing is filtered but only the molecules are ordered in increasing dG order in the `ordered_output*` files.   
   7) _**<path_to_directory_where_you_want_filtered_results>**_: This is the fifth argument the `filtering.R` takes and the sixth that `Rstudio` takes. You can actually 
put the path to any directory in which you want the filtered molecules - and output pdf files with filtered molecules - to be saved. If you want, you can take advantage 
of `VSpipe` creating the `filtered_results` directory and you can use it, if you want to.

---------------------------------------

Now that we know what each argument means, let's see an example of how you could run it. 
For instance, if you had the `filtering.R` script in `~/Applications/VSpipe/Tools` and if you had the following architecture file in a directory
called `Test_VSpipe` in which you have already run VSpipe...

```
Test_VSpipe 
	|
	|- ligands 
	|- receptor 
	|- results 
	|       |- config_vina 
	|       |- filtered_results 
	|       |- lowest_energy_pdb 
	|       |- pdbqt_lip_rules 
	|       |- vina_log 
	|       |- vina_pdbqt 
	|       |- *pdf 
	|       |- ordered_output.tsv
	|       |- ordered_output.csv
	|       |- ordered_output_ATLAS.txt
	|       |- output.csv	
	|       |- output.tsv	
	|       
	|- logfile.txt
	|- variables.txt
```

... then you could open a terminal inside `Test_VSpipe/results` (or type `cd` to move to that specific directory) and then run the `filtering.R` like this: 

```

Rscript ~/Applications/VSpipe/Tools/filtering.R  results/ 8 ">-5" 1 filtered_results/ 

```

In this case, I want:   
   * To filter... *(I have **1** as the 5th argument and not a **0**, that is why I know I want to filter)*   
   * ... the molecules according to dG *(according to dF because this is what the **8** as a 3rd argument does)*   
   * ... that are larger than -5 *(this is what **">-5"** does as a 4th argument)*   
   * ... and save the output files and filtered molecules in `filtered_results/` *(it assumes you have in the directory from where you are running this command a directory called `filtered_results`)*   


And this is it! Now you can filter your results according to different parameters and using different threshold!
