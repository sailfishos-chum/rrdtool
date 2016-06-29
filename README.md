# pkg-rrdtool
RPM packaging of rrdtool for Sailfish. This project consists of RPM spec file and small tools for working with rrdtool in Sailfish

## To build RRDtool

Download the source of rrdtool that you want to build and unzip it. Make a directory under extracted source directory called pkg-rrdtool (or use symbolic links) and download all files from this repo to that folder. Then make in MER SDK, make RPM as usual (cd to top rrdtool source directory):

    mb2 -t SailfishOS-i486 -s pkg-rrdtool/rrdtool.spec build -j4
