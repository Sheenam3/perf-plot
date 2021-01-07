#!/bin/bash    
#Plot and compare two processes using its CPU usage and memory usage by psrecord, this will give you two separate graphs
#Usage ./plot.sh process_name1 pid1 process_name2 pid2
#Get pid by using 'ps aux | grep process_name'
pname1=$2
pname2=$4
psrecord $(pgrep $pname1) --interval 1 --duration 60 --plot $pname1.png &
P1=$1
psrecord $(pgrep $pname2) --interval 1 --duration 60 --plot $pname2.png &
P2=$3
wait $P1 $P2
echo 'Done'
