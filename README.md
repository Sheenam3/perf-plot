# perf-plot
About
=====
perf-plot contains few scripts to get the performance analysis of a process or more than one processes in terms of CPU usage.
These scripts are helpful in obtaining a comparison chart also.

``plot-files`` is a small python script to plot the CPU 
activity of a process using ``psrecord``. This is still under development and experimental.

The code is released under a Simplified BSD License, which is given in
the ``LICENSE`` file.

Requirements
============

-  Python 2.7 or 3.3 and higher
-  `psrecord <https://github.com/astrofrog/psrecord>`
-  `matplotlib <http://www.matplotlib.org>`__ (optional, used for
   plotting)

Installation
============

1. Install psrecord & required libraries

::

    pip install psrecord
    apt-get install python-matplotlib python-tk
    
2. clone this repository on your system

Usage
=====

Basics
------
This script is basically for capturing processes cpu usage and comparing them in a single chart.

`plot.sh` is a script used for plotting two processes and get its log files.

`get-logs.sh` is used to get a log file of two processes

`plot-files.py` is a script to plot cpu comparison among the processes by simply passing log file names which we get using the above files.

To plot a comparison we need log files of the processes. In this case, after running the following command two processes log files `process_name.txt` will be present in your current directory:



::
    `./get-logs.sh pid_of_process1 process_name1 pid_of_process2 process_name2`


Plotting
--------

To make a plot of the activity:

::

    python plot-files.py process_name1.txt process_name2.txt

This will produce a plot such as:

![comparison](https://github.com/Sheenam3/perf-plot/blob/master/doc/plot-file-compare.png)





