#!/usr/bin/python
#Usage : python plot-files.py filename1.txt filename2.txt
import sys
import matplotlib.pyplot as plt
import numpy as np


file1=sys.argv[1]
file2=sys.argv[2]
#file3=$3
fn=[file1, file2]

#create a figure for plotting graphs
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_ylabel('CPU (%)', color='b')
ax.set_xlabel('time(s)', color= 'b')
i=0

for fname in fn:
    #Parse data from the file1
    data=np.loadtxt(fname)
    x1=data[:,0]
    y1=data[:,1]
    ax.set_ylim(0.,max(y1) * 1.2)
    head, sep, tail = fname.partition('.')
    #To display plot line in different colors
    if i == 1:
        ax.plot(x1,y1,'-',lw=1,color='b', label=head)
    else:
        ax.plot(x1,y1,'-',lw=1,color='r', label=head)
    i += 1

ax.legend()
ax.grid()
#title of the graph
fig.suptitle('CPU Usage Comparison(%)')
#filebane to be saved
fig.savefig('test.png')
