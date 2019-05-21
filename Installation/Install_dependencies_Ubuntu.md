#  Install VSpipe on Linux distributions - tested on Ubuntu only!

## Installing MGLTools

First, go to [their website](http://mgltools.scripps.edu/downloads/latest) and download the [Linux release](http://mgltools.scripps.edu/downloads/tars/releases/nightly/latest/REL/mgltools_x86_64Linux2_latest.tar.gz)
This installation procedure assumes that:   
   1. You have already cloned this repository (e.g., you might see `VSpipe-master`).   
   2. You have downloaded the `VSpipe.tar.gz` file from [releases](https://github.com/sabifo4/VSpipe/releases/tag/v1.0), untarred it,   and you have saved it in this cloned directory (e.g., `VSpipe-master/VSpipe`).   
   3. You have downloaded the `mgltools_x86_64Linux2_latest.tar.gz`, untarred it, and saved it inside the untarred `VSpipe.tar.gz`. Assuming you have saved `VSpipe` inside `VSpipe-master`, you should have the `MGLTools` software saved as `VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest`.

Let's consider that you have decided to clone this repository (e.g., `VSpipe-master`) inside `~/Applications`.
Therefore, before starting with the `MGLTools` installation, you should make sure your directory architecture looks like 
something such as: 

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
      |     |- mgltools_x86_64Linux2_latest.tar.gz
      | 
      |- README.md
		  
```

*Note: Depending on how you have cloned this repository, you might see `VSpipe` instead of `VSpipe-master`*

Once you make sure that everything is ready, then follow the next commands. 
Make sure that you do not just copy and paste, as here we assume the file architecture described 
above (i.e., `~/Applications/VSpipe-master/VSpipe`). **If you have saved `VSpipe` somewhere else, please make sure that you change the paths described in the installation procedure below so it matches your path**

```
cd ~/Applications/VSpipe-master/VSpipe
tar -xzvf mgltools_x86_64Linux2_latest.tar.gz
chmod +x  mgltools_x86_64Linux2_latest
cd mgltools_x86_64Linux2_latest/
tar -xzvf MGLToolsPckgs.tar.gz
```

After that, please export the path to your `~/.bashrc`. You can open this file with your 
preferred text editor (e.g., `vim`, `nano`, `atom`, etc.) and add the path or you can just type the following 
command in the terminal :

```
# Run this to export the path to your ~/.bashrc
echo "export PATH=$PATH:~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest" >> ~/.bashrc
```

Now, make sure you are still at `~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest` 
and then, from the terminal, execute the `install.sh` script:

```
# Our current directory is: ~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest
./install.sh
```

---

*NOTE: If you get an error message about line 78, you should use the next command. It will comment this line and 
add a new command that makes the installation procedure work*: 
```
sed -i 's/export\ PATH\=\"\$MGL\_ROOT\/bin\:\"\$PATH/\#export\ PATH\=\"\$MGL\_ROOT\/bin\:\"\$PATH\ \#\ SAC\:\ original\ line\ commented\
	\necho\ \"export\ PATH\=\$PATH\:\$MGL\_ROOT\/bin\"\ \>\>\ \~\/\.bashrc\ \#\ SAC\: new\ line\ added/' install.sh
```

*After that, you can rerun the script `./install.sh` and it should install `MGLTools` without errors.*.

---

You will see how several messages are printed out in your terminal as `MGLTools` is being installed. At the end 
of the installation, you will see some instructions about adding the following aliases to your `~/.bashrc`. 
If you have downloaded the `mgltools_x86_64Linux2_latest` version, you should see something like this: 

```
alias pmv='~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest/bin/pmv'
alias adt='~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest/bin/adt'
alias vision='~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest/bin/vision'
alias pythonsh='~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest/bin/pythonsh'
```

Again, open your `~/.bashrc` and add the aliases you have been asked 
to append to this file at the end of the `MGLTools` installation.

Subsequently, without changing directory, type the following on the terminal: 

```
# Our current directory is: ~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest
source ./initMGLtools.sh   
```

Then, append to the `~/.bashrc` the following path - make sure you 
use the correct path according to where you have installed `VSpipe`: 

```
export PYTHONPATH="~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest/MGLToolsPckgs"
```

## Installing AutoDock tools 

### AD4 

Download AD4 tools `autogrid4` and `autodock4` for Linux:

```
cd ~/Applications/VSpipe-master/VSpipe/
wget http://autodock.scripps.edu/downloads/autodock-registration/tars/dist426/autodocksuite-4.2.6-x86_64Linux2.tar
tar -xvf autodocksuite-4.2.6-x86_64Linux2.tar
```

Once it is downloaded, copy both `autogrid` and `autodock4` in the `~/Applications/VSpipe-master/VSpipe/Tools` directory:
If you want, you can then clean this directory by removing the tar and untarred files with the 
`AD4` tools (last two comments in the next snippet):

```
# Our current directory is "~/Applications/VSpipe-master/VSpipe/"
cp ~/Applications/VSpipe-master/VSpipe/x86_64Linux2/autodock4 ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/x86_64Linux2/autogrid4 ~/Applications/VSpipe-master/VSpipe/Tools

# Clean directory - remove unnecessary files and/or directories
rm -r ~/Applications/VSpipe-master/VSpipe/x86_64Linux2
rm autodocksuite-4.2.6-x86_64Linux2.tar
```

### Vina
Go to the [Vina website](http://vina.scripps.edu/download.html) and download the corresponding Vina files
for Linux (you can also download this by clicking [here](http://vina.scripps.edu/download/autodock_vina_1_1_2_linux_x86.tgz)). After that, copy both executables `vina` and `vina_split` in the `~/Applications/VSpipe-master/VSpipe/Tools` 
directory:

```
# Our current directory is "~/Applications/VSpipe-master/VSpipe/"
tar -xzvf autodock_vina_1_1_2_linux_x86.tgz
cp ~/Applications/VSpipe-master/VSpipe/autodock_vina_1_1_2_linux_x86/bin/vina ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/autodock_vina_1_1_2_linux_x86/bin/vina_split ~/Applications/VSpipe-master/VSpipe/Tools

# Clean directory - remove unnecessary files and/or directories 
rm -r autodock_vina_1_1_2_linux_x86
rm autodock_vina_1_1_2_linux_x86.tgz
```

### AutoDock python scripts
Now, copy the files `prepare_dpf4.py`, `prepare_gpf4.py`, `prepare_ligand4.py`, `prepare_receptor4.py`,
and `summarize_results4.py` to `mgltools_x86_64Linux2_latest/MGLToolsPckgs`.
They are located in `mgltools_x86_64Linux2_latest/MGLToolsPckgs/AutoDockTools/Utilities24/"

```
cp ~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_dpf4.py ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/mgltools_x86_64Linux2_latest/MGLToolsPckgs/AutoDockTools/Utilities24/summarize_results4.py ~/Applications/VSpipe-master/VSpipe/Tools
```

### Give permissions to execute !
Do not forget to give permissions to all the scripts in the `Tools` directory!

```
chmod 775 ~/Applications/VSpipe-master/VSpipe/Tools
```


## Installing OpenBabel  

Before going through the OpenBabel installation, there are some additional packages that you might want to install if 
you want to have OpenBabel with all the features it can offer:

```
# Install CMake 2.4.8 or later
sudo apt-get install cmake

# Install cairo library and libpython-dev
sudo apt-get install libpython-dev
sudo apt-get install libcairo2-dev

# Install Eigen 3.0 or later 
sudo apt-get install libeigen3-dev

# Install libxml2 
sudo apt-get install libxml2-dev

# Install zlib
sudo apt-get install zlib1g-dev

# Install wxWidgets 2.8 
sudo apt-get install libwxgtk3.0-dev
```

After that, you can go to the [OpenBabel website](http://openbabel.org/wiki/Category:Installation), download 
OpenBabel (you can also find all the previous versions of OpenBabel [here](https://sourceforge.net/projects/openbabel/files/openbabel/))
and follow the instructions to compile OpenBabel [here](https://open-babel.readthedocs.io/en/latest/Installation/install.html#compiling-open-babel).

Here, you have a summary of the basic OpenBabel installation. If you want an advanced installation, check their
INSTALL file or the link provided above.

*NOTE: The following instructions assume that the OpenBabel source distribution is in 
the directory ~/Applications/VSpipe-master/VSpipe/openbabel-2.4.1.*

```
# 1. Create a 'build' directory:
cd ~/Applications/openbabel-2.4.1
mkdir build
cd build

# 2. Configure the build system. You can specify additional build
#    options at this time (see below):
cmake ..

# 3. Compile:
make -j2

# 4. Test (optional):
make test

# 5. Install:
sudo make install
```

---

_**(OPTIONAL) Installing Anaconda**_   
If you have already installed Python 2.7, `VSpipe` and the AutoDock scripts it relies on should work without any issue.
Nevertheless, if you would like to have Anaconda installed, you can download the Linux release [here](https://www.anaconda.com/download/#download)
Just follow the instructions of the installer [here](https://conda.io/docs/user-guide/install/linux.html)
and then run the bash script you would have previously downloaded 

```
bash Anaconda-latest-Linux-x86_64.sh
```

---

## Problems with Numpy

Apparently, there is a problem with the new version of Numpy (numpy>1.9) when you run some of the 
AutoDock python scripts because it does not support `numpy.oldnumeric`. In Bitbucket, 
see the discussion [here](https://bitbucket.org/khinsen/scientificpython/issues/13), 
they make some suggestions about how to deal with this particular issue. We decided to install a lower version of numpy  
so the AutoDock scripts could work:

```
pip install "numpy<1.9"
``` 

## Adding VSpipe to your path 
You might be keen on adding an alias to run `VSpipe` from any directory by just typing 
`VSpipe` on the terminal. If that is your case, open your `~/.bashrc` with 
your preferred text editor and type the following (note that the path is the one used in the examples above,
just modify it according to yours): 

```
alias VSpipe='~/Applications/VSpipe-master/VSpipe/Tools/VSpipe'
```

---

If you have managed to install these third-party tools, now you should be able to open a terminal on 
your working directory, type `VSpipe`, and get the pipeline started.

Happy docking! :)


