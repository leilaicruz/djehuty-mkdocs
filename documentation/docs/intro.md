Chapter 1Introduction
---------------------


djehuty is the data repository system developed by and for 4TU.ResearchData. The name finds its
inspiration in [Thoth](https://en.wikipedia.org/wiki/Thoth), the Egyptian entity that introduced the idea of writing.
### 1\.1  Obtaining the source code


The source code can be downloaded at the
[Releases](https://github.com/4TUResearchData/djehuty/releases)[1](djehuty2.html#fn1x1) 
page. Make sure to download the djehuty\-24\.10\.1\.tar.gz file.
Or, directly download the tarball using the command\-line:


```
curl -LO https://github.com/4TUResearchData/djehuty/releases/\  
download/v24.10.1/djehuty-24.10.1.tar.gz
```

After obtaining the tarball, it can be unpacked using the tar command:


```
tar zxvf djehuty-24.10.1.tar.gz
```

### 1\.2  Installing the prerequisites


The djehuty program needs Python (version 3\.8 or higher) and Git to be installed. Additionally, a couple
of Python packages need to be installed. The following sections describe installing the prerequisites on
various GNU/Linux distributions. To put the software in the context of its environment, figure [1\.1](#x1-5001r1) displays
the complete run\-time dependencies from djehuty to glibc.


---




 ![PIC](figures/0457dd27_1.png)





  
    Figure 1\.1: Run\-time references when constructed with the packages from GNU Guix.   



---


The web service of djehuty stores its information in a SPARQL 1\.1 ([“SPARQL 1\.1 Overview”](#Xsparql-11), [2013](#Xsparql-11)) endpoint. We recommend
either [Blazegraph](https://blazegraph.com/)[2](djehuty3.html#fn2x1) or [Virtuoso
open\-source edition](http://vos.openlinksw.com/owiki/wiki/VOS)[3](djehuty4.html#fn3x1) .
#### 1\.2\.1  Installation on Enterprise Linux 7\+


The Python packages on Enterprise Linux version 7 or higher seem to be too far out of date. So installing
the prerequisites involves two steps.
The first step involves installing system\-wide packages for Python and Git.


```
yum install python39 git
```

The second step involves using Python’s venv module to install the Python packages in a virtual
environment:


```
python3.9 -m venv djehuty-env 
. djehuty-env/bin/activate 
cd /path/to/the/repository/checkout/root 
pip install -r requirements.txt
```


### 1\.3  Installation instructions


After obtaining the source code (see section [1\.1](#x1-40001.1) ‘[Obtaining the source code](#x1-40001.1)’) and installing the
required tools (see section [1\.2](#x1-50001.2) ‘[Installing the prerequisites](#x1-50001.2)’), building involves running the following
commands:


```
cd djehuty-24.10.1 
autoreconf -vif # Only needed if the "./configure" step does not work. 
./configure 
make 
make install
```

To run the make install command, super user privileges may be required. Specify a \-\-prefix to the
configure script to install the tools to a user\-writeable location to avoid needing super user
privileges.
After installation, the djehuty program will be available.

### 1\.4  Pre\-built containers


4TU.ResearchData provides Docker container images as a convenience service for each monthly djehuty release.
The following table outlines the meaning of each image provided. The images are published to [Docker
Hub](https://hub.docker.com/r/4turesearchdata/djehuty)[4](djehuty5.html#fn4x1) .
 

| Image tag | Description |
| devel | Image meant for development purposes. Before it executes the djehuty  command it checks out the latest codebase. So re\-running the same  container image may result in running a different version of djehuty. |
| latest | This image points to the latest djehuty release. It does not automatically  update the djehuty codebase. |
| XX.X | 4TU.ResearchData releases a version each month where the number before  the dot refers to the year and the number after the dot refers to the month.  Use a specific version image when you want to upgrade at your own pace. |
|  |

 
To build the container images for yourself, see the build instructions in the ‘docker/Dockerfile’
file.
