#!/usr/bin/python
#Usage : python plot.py filename1.txt filename2.txt
import sys
import matplotlib.pyplot as plt
import numpy as np

fn=[]

#To check the number of files passed in argument
for i in range(len(sys.argv)):
    if i!=0:
        n = i
        filen = sys.argv[n]
        fn.append(filen)
    else:
        continue

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


#plot1
    ax.set_ylim(0.,max(y1) * 1.2)
    head, sep, tail = fname.partition('.')
    if i == 1:
        ax.plot(x1,y1,'-',lw=1,color='b', label=head)
    elif i==2:
        ax.plot(x1,y1,'-',lw=1,color='r', label=head)
    else:
        ax.plot(x1,y1,'-',lw=1,color='g', label=head)
    i += 1
ax.legend()
ax.grid()

fig.suptitle('CPU Usage Comparison(%)')
fig.savefig('plot-file.png')
