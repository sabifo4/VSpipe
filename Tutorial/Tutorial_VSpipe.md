## __Download VSpipe local__

First of all, you should clone this repository in your local PC. You can download it 
as a zip file by clicking either the `Clone or download` button in the Git repository or [here](https://github.com/sabifo4/VSpipe/archive/master.zip).
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
	  |     |- VSpipe_details.docx
      | 
	  |- Tutorial 
	  |     |- Tutorial_VSpipe.md
      | 
      |- README.md
      |- Tutorial_VSpipe.md	  
```

Once you have cloned this repository, you can find the source code for each operating system under the `release` ([Mac OS X](), [Linux](), [WLS]()). 
Once you have downloaded  the corresponding `zip` file, please unzip it and save it inside this GitHub repository. If you saved the GitHub repository 
under the `~/Applications` directory, you should have something like this once you have untarred the `zip` file: 

```  
Applications
  |- VSpipe-master 
      |- .git 
      |- Installation 
      |     |- Install_dependencies_MacOSX.md 
      |     |- Install_dependencies_Linux.md 
      |     |- Install_dependencies_WLS.md 
	  |     |- VSpipe_details.docx
	  | 
	  |- Tutorial 
	  |     |- Tutorial_VSpipe.md
      | 
      |- VSpipe
      |     |- Tools 
      | 
      |- README.md	  
```

After that, please follow the installation instructions for your operating system to install the third-party 
tools `VSpipe` relies on:   

   1. Installation for Linux *- only tested on Ubuntu but should work for any Linux distribution*: click [here]().   
   2. Installation for WLS: click [here]()   
   3. Installation for Mac OS X: click [here]()   
   
If you have followed the steps described in the installation file, you might have an alias to run 
`VSpipe` on the terminal just by typing `VSpipe` on the terminal. If you have already typed `VSpipe` on 
your terminal and you see this message:   

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

Then you can follow the tutorial in the next section! Otherwise, you might have missed an important step 
during the installation of the third-party tools.


## __Run VSpipe local__

### 1. Set the working directory

First of all, set your working directory. Open a terminal in your preferred location and 
create your working directory. In this tutorial, the working directory is going to be called `test_VSpipe`,
although you can change its name. Note that this will not change the next steps in the tutorial.
The path to `test_VSpipe` for this example is `/home/user/my_dockings/test_VSpipe`, hence:

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

1. Make sure you are in your working directory

```bash
$ pwd 
/home/user/my_dockings/test_VSpipe
```

2. Run VSpipe for the first time

```bash
$ VSpipe
```
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
VSpipe before, please type `no` as you need to clean the PDB file with your 
target protein. After typing `no` and pressing `ENTER` (RETURN key), you are asked the following 
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
with your target protein is **`3X4P.pdb`**. In order 