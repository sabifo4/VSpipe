#  Install VSpipe on Mac OS X  

## Installing MGLTools

First, go to [their website](http://mgltools.scripps.edu/downloads) and download the [Mac OS X release](http://mgltools.scripps.edu/downloads/downloads/tars/releases/REL1.5.6/mgltools_i86Darwin9_1.5.6.tar.gz)
This installation procedure assumes that:   
   1. You have already cloned this repository (e.g., you might see `VSpipe-master`).   
   2. You have downloaded the `VSpipe.tar.gz` file from [releases](https://github.com/sabifo4/VSpipe/releases/tag/v1.0), untarred it,   and you have saved it in this cloned directory (e.g., `VSpipe-master/VSpipe`).   
   3. You have downloaded the `mgltools_i86Darwin9_1.5.6.tar.gz`, untarred it, and saved it inside the untarred `VSpipe.tar.gz`. Assuming you have saved `VSpipe` inside `VSpipe-master`, you should have the `MGLTools` software saved as `VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6`.

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
      |     |- VSpipe_details.docx
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
tar -xzvf mgltools_i86Darwin9_1.5.6.tar.gz
chmod +x  mgltools_i86Darwin9_1.5.6
cd mgltools_i86Darwin9_1.5.6/
tar -xzvf MGLToolsPckgs.tar.gz
```

After that, please export the path to your `~/.bashrc` or `~/.bash_profile`. You can either open one of these files with your 
preferred text editor (e.g., `vim`, `nano`, `atom`, etc.) and add the path or you can just type one of the following 
commands in the terminal (depending on the file where you want to export the path):

```
# Run this if you want to export the path to your ~/.bashrc
echo "export PATH=$PATH:~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6" >> ~/.bashrc

# Run this if you want to export the path to your ~/.bash_profile
echo "export PATH=$PATH:~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6" >> ~/.bash_profile
```

Now, make sure you are still at `~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6` 
and then, from the terminal, execute the `install.sh` script:

```
# Our current directory is: ~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6
./install.sh
```

You will see how several messages are printed out in your terminal as `MGLTools` is being installed. At the end 
of the installation, you will see some instructions about adding the following aliases to your `~/.bashrc`. 
If you have downloaded the `mgltools_i86Darwin9_1.5.6` version, you should see something like this: 

```
alias pmv='~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/bin/pmv'
alias adt='~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/bin/adt'
alias vision='~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/bin/vision'
alias pythonsh='~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/bin/pythonsh'
```

Again, open either your `~/.bashrc` or your `~/.bash_profile` and add the aliases you have been asked 
to append to these files at the end of the `MGLTools` installation.

Subsequently, without changing directory, type the following on the terminal: 

```
# Our current directory is: ~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6
source ./initMGLtools.sh   
```

Then, append to either the `~/.bash_profile` or the `~/.bashrc` the following path - make sure you 
use the correct path according to where you have installed `VSpipe`: 

```
export PYTHONPATH="~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/MGLToolsPckgs"
```

## Installing AutoDock tools 

### AD4 

Download AD4 tools `autogrid4` and `autodock4` for Mac OS X:

```
cd ~/Applications/VSpipe-master/VSpipe/
wget http://autodock.scripps.edu/downloads/autodock-registration/tars/dist426/autodocksuite-4.2.6-MacOSX.tar
tar -xvf autodocksuite-4.2.6-MacOSX.tar
```

Once it is downloaded, copy both `autogrid` and `autodock4` in the `~/Applications/VSpipe-master/VSpipe/Tools` directory:
If you want, you can then clean this directory by removing the tar and untarred files with the 
`AD4` tools (last two comments in the next snippet):

```
# Our current directory is "~/Applications/VSpipe-master/VSpipe/"
cp ~/Applications/VSpipe-master/VSpipe/MacOSX/autodock4 ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/MacOSX/autogrid4 ~/Applications/VSpipe-master/VSpipe/Tools

# Clean directory - remove unnecessary files and/or directories
rm -r ~/Applications/VSpipe-master/VSpipe/MacOSX
rm autodocksuite-4.2.6-MacOSX.tar
```

### Vina
Go to the [Vina website](http://vina.scripps.edu/download.html) and download the corresponding Vina files
for Mac OS X (you can also download this by clicking [here](http://vina.scripps.edu/download/autodock_vina_1_1_2_mac.tgz)). After that, copy both executables `vina` and `vina_split` in the `~/Applications/VSpipe-master/VSpipe/Tools` 
directory:

```
# Our current directory is "~/Applications/VSpipe-master/VSpipe/"
tar -xzvf autodock_vina_1_1_2_mac.tgz
cp ~/Applications/VSpipe-master/VSpipe/autodock_vina_1_1_2_mac/bin/vina ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/autodock_vina_1_1_2_mac/bin/vina_split ~/Applications/VSpipe-master/VSpipe/Tools

# Clean directory - remove unnecessary files and/or directories 
rm -r autodock_vina_1_1_2_mac
rm autodock_vina_1_1_2_mac.tgz
```

### AutoDock python scripts
Now, copy the files `prepare_dpf4.py`, `prepare_gpf4.py`, `prepare_ligand4.py`, `prepare_receptor4.py`,
and `summarize_results4.py` to `~/Applications/VSpipe-master/VSpipe/Tools`.
They are located in `~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/"

```
cp ~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_dpf4.py ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py ~/Applications/VSpipe-master/VSpipe/Tools
cp ~/Applications/VSpipe-master/VSpipe/mgltools_i86Darwin9_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/summarize_results4.py ~/Applications/VSpipe-master/VSpipe/Tools
```

### Give permissions to execute !
Do not forget to give permissions to all the scripts in the `Tools` directory!

```
chmod 775 ~/Applications/VSpipe-master/VSpipe/Tools
```


## Installing OpenBabel  

If you want to install OpenBabel, you can follow the instructions [here](http://openbabel.org/wiki/Category:Installation).
We recommend you install it with `HomeBrew`:

```
brew install open-babel  
```

If you had problems to install OpenBabel with `HomeBrew`, you can always compile it from source as described in their 
installation website. If you choose this alternative installation, once you have the tar file with the source code 
you can use the following commands (please see their website for more advanced options during compilation):

```
# Location of your OpenBabel is ~/Applications/VSpipe-master/VSpipe/
# If you had v2.4.1 and you had directory called `openbabel-2.4.1` ...
cd openbabel-2.4.1
mkdir -p build && cd build
cmake -DCMAKE_INSTALL_PREFIX=~/Applications/VSpipe-master/VSpipe/openbabel_v2.4.1 ..
make && make install

# Clean directories
rm -rf ~/Applications/VSpipe-master/VSpipe/openbabel-2.4.1
```

--- 

_**(OPTIONAL) Installing Anaconda**_   
If you have Python installed on your PC, Anaconda is not needed by `VSpipe`. 
Nevertheless, if you do not have Anaconda but you would like to have it, you can download the Mac OS X release [here](https://www.anaconda.com/download/#download)
Just follow the instructions of the installer - it should be an easy procedure! 

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
`VSpipe` on the terminal. If that is your case, open either your `~/.bash_profile` or your `~/.bashrc` with 
your preferred text editor and type the following (note that the path is the one used in the examples above,
just modify it according to yours): 

```
alias VSpipe='~/Applications/VSpipe-master/VSpipe/Tools/VSpipe'
```

---

If you have managed to install these third-party tools, now you should be able to open a terminal on 
your working directory, type `VSpipe`, and get the pipeline started.

Happy docking! :)

