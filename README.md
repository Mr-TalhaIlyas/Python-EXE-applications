# Python-EXE-applications
Convert python scripts to exe files.

## Steps 

First write your scripts and test them fully. Use relative paths in the scripts to locate the file. See the scripts in the repo.

Now install the application to convert the python script to exe file.

**Important** inside the same `env` where you built and tested you scripts.

```
pip install auto-py-to-exe
```
and then run
```
auto-py-to-exe
```
and set the settings as follows.

![alt text](https://github.com/Mr-TalhaIlyas/Python-EXE-applications/blob/main/screen/s1.png)

## PyInstaller EXE command

```
pyinstaller --noconfirm --onedir --windowed --icon "C:/Users/talha/Downloads/Tomography/gui 2/production/blood.ico" --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/b_feats.npy;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/b_lbls.npy;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/b_model.h5;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/blood.ico;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/blood.png;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/c_feats.npy;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/c_lbls.npy;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/c_model.h5;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/company.png;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/gui.py;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/helpers.py;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/inference.py;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/loading.gif;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/place_holder1.PNG;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/place_holder2.PNG;." --add-data "C:/Users/talha/Downloads/Tomography/gui 2/production/rv.ico;." --hidden-import="sklearn.utils._cython_blas" --hidden-import="sklearn.neighbors.typedefs" --hidden-import="sklearn.neighbors.quad_tree" --hidden-import="sklearn.tree._utils" --hidden-import="sklearn.utils._typedefs" --hidden-import="sklearn.neighbors._partition_nodes" "C:/Users/talha/Downloads/Tomography/gui 2/production/gui.py"

```
 
## Working application and weights

[Google Drive](https://drive.google.com/drive/u/2/folders/1PCwoMVl6RjRO6lLEHxiWG_MJ5jwiKJGP)
