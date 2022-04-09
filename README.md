### Configure Rosetta for the tesis

#### Install Rosetta

1. **Requirements**
* Have Python-3 installed

2. **Download Rosetta**
* Go to [Rosetta](https://www.rosettacommons.org/software/license-and-download)
* Click in *Academic Download*
* **User**: Academic_User **Password**: Xry3x4
* Click in *Download Rosetta 3.13*
* Download *Rosetta 3.13 source - as one bundle (5.2G)* 

3. **Install Packages**

* *apt install zlib1g-dev*
* *apt install scons*
* *apt install build-essential*

4. **Install Rosetta**

* Go to the folder where you downloaded rosetta
* *tar -xvzf rosetta[releasenumber].tar.gz*
* *cd rosetta*/main/source*
* *./scons.py mode=release bin*.
* Check the a *bin* folder was created

