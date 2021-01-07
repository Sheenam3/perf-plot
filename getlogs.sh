#!/bin/bash    
pname1=$2
pname2=$4
psrecord $(pgrep $pname1) --interval 1 --duration 60 --log $pname1.txt &
P1=$1
psrecord $(pgrep $pname2) --interval 1 --duration 60 --log $pname2.txt &
P2=$3
wait $P1 $P2
echo 'Done'
~             
