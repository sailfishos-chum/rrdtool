# pkg-rrdtool
RPM packaging of rrdtool for Sailfish. This project consists of RPM spec file and small tools for working with rrdtool in Sailfish

## To build RRDtool

Download the source of rrdtool that you want to build and unzip it. Make a directory under extracted source directory called pkg-rrdtool (or use symbolic links) and download all files from this repo to that folder. Then make in MER SDK, make RPM as usual (cd to top rrdtool source directory):

    mb2 -t SailfishOS-i486 -s pkg-rrdtool/rrdtool.spec build -j4

## rrd-sync

This is a small utility that transfers RRD files between hosts with different architectures. This script transfers all RRDs in the given directory in LOCALHOST to the specified directory on specified host. The structure of local directory is transferred as well. Internally, it uses SSH to transfer the data. For convenience, insure that you could login into the specified host using SSH keys. The remote and local hosts have to have RRDTOOL installed. If the remote host doesn't have RRDtool installed, you could run the generated .sh script later to convert all xml.gz files into .rrd
