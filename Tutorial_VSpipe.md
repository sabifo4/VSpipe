## __Download VSpipe local__

First of all, you should clone this repository in your local PC. You can download it 
as a zip file by clicking either the `Clone or download` button in the Git repository or [here](https://github.com/sabifo4/VSpipe/archive/master.zip).
If you have `git` installed, you can also create a directory in your local PC to where you
want to save it, and type the following in a terminal:

`git clone https://github.com/sabifo4/VSpipe`

This repository consists of the following:

```
VSpipe 
    |- Tools 
    |    |- *Many txt and py files the user should **not** use* 
    |	 |- VSpipe_targeted *(VSpipe script to run targeted docking)*
    |	 |- VSpipe_blind    *(VSpipe script to run blind docking)*
    |	 |- filtering.py    *(VSpipe script to filter the results of a VSpipe run)*
    |
    |- Documentation.docx
    |- Install_dependencies.txt
    |- README.md
    |- Tutorial_VSpipe.md
```

Once you have cloned this repository, you can find the scripts to run `VSpipe` in the directory called 
**Tools**. In case the files saved in this directory do not have full permissions, please
give full permissions as it follows. For this tutorial, we will let the path to the cloned 
repository be `/home/Applications/VSpipe`. Taking this into account, we should type

```bash 
$ cd /home/Applications/VSpipe
$ chmod 775 Tools
```

## __Install VSpipe dependencies__ 

Follow the instructions detailed in the [__Install_dependencies.txt__](https://github.com/sabifo4/VSpipe/blob/master/Install_dependencies.txt)
file. Once you have cloned this repository and MGLTools, OpenBabel, and Anaconda are installed, you can proceed to run VSpipe.

**NOTE**: When installing Anaconda, it is very important that you check the Numpy version you install, as detailed from line 179
onwards in the [__Install_dependencies.txt__](https://github.com/sabifo4/VSpipe/blob/master/Install_dependencies.txt)
file. The AutoDock scripts use the `numpy.oldnumeric` module and only work when the Numpy version installed is lower than v1.9.
We explain this as well in the file mentioned above, but you can check [this site](https://bitbucket.org/khinsen/scientificpython/issues/13))
for more information on the issue.


## __Run VSpipe local__

#### 1. Set the working directory

Once the permissions to this directory have been given, you should be able to run `VSpipe`.
First of all, set your working directory. Open a terminal in your preferred location and 
create your working directory. In this tutorial, the working directory is going to be called **test_VSpipe**,
although you can change its name. Note that this will not change the next steps in the tutorial. For example, if
**test_VSpipe** was to be created in */home/user/wd*, then we can create our working directory and move into
it as it follows:

```bash
$ pwd
/home/user/wd
$ mkdir test_VSpipe
$ cd test_VSpipe 
$ pwd
/home/user/wd/test_VSpipe
```

#### 2. Run a virtual screening with VSpipe
Once you are inside your working directory, you are ready to run `VSpipe`. You should type the whole path to the bash 
script `VSpipe` (for targeted docking) or to the bash script `VSpipe_blind` (for blind docking)
which are stored in `VSpipe/Tools`. If it is properly working, the following message will appear 
in both cases:

```bash
# Case 1: Run targeted docking from your working directory
$ pwd 
/home/user/wd/test_VSpipe
$ /home/Applications/VSpipe/Tools/VSpipe

Please type the full path where the prepare_dpf4.py, prepare_gpf4.py,
prepare_ligand4.py, and prepare_receptor4.py are. After that, please 
press [ENTER]:


# Case 2: Run blind docking from your working directory
$ pwd 
/home/user/wd/test_VSpipe
$ /home/Applications/VSpipe/Tools/VSpipe_blind

Please type the full path where the prepare_dpf4.py, prepare_gpf4.py,
prepare_ligand4.py, and prepare_receptor4.py are. After that, please 
press [ENTER]:

```

If you do not want to type the absolute path everytime you want to run 
`VSpipe`, you can always create an alias in your `.bashrc`. You can open
this file with your favourite text editor and add the following lines:

```bash
alias VSpipe_t="/home/Applications/VSpipe/Tools/VSpipe_targeted"
alias VSpipe_b="/home/Applications/VSpipe/Tools/VSpipe_blind"
```

We have chosen to use the alias `VSpipe_t` to call the script that runs targeted docking and 
`VSpipe_b` the one who runs blind docking. Nevertheless, note that you can choose the name you 
prefer to use to run both dockings.

#### 3. Set the path to the AutoDock scripts 

If you have properly installed the dependencies VSpipe needs as it is 
detailed in the [__Install_dependencies.txt__](https://github.com/sabifo4/VSpipe/blob/master/Installation_Ubuntu.txt)
file, then the `prepare_dpf4.py`, `prepare_gpf4.py`, `prepare_ligand4.py`, and `prepare_receptor4.py`
should be in `/home/Applications/VSpipe/mgltools_x86_64Linux2_latest/MGLToolsPckgs`. If you changed the path 
to where MGLTools were to be installed, then just change the absolute path accordingly.
For this tutorial, we will keep the path as detailed in the [__Install_dependencies.txt__](https://github.com/sabifo4/VSpipe/blob/master/Installation_Ubuntu.txt)
file. Therefore, once VSpipe starts, you should type this absolute path as it follows:

```bash
# Example: Run targeted docking from your working directory
$ pwd 
/home/user/wd/test_VSpipe
$ /home/Applications/VSpipe/pidock/VSpipe

Please type the full path where the prepare_dpf4.py, prepare_gpf4.py,
prepare_ligand4.py, and prepare_receptor4.py are. After that, please 
press [ENTER]:
/home/Applications/VSpipe/mgltools_x86_64Linux2_latest/MGLToolsPckgs

```

After that, just follow the instructions `VSpipe` will be printing on the screen in 
order to proceed with the virtual screening!

