#!/bin/bash
#Usage: ./get-logs.sh pid1 process_name1 pid2 process_name2
pname1=$2
pname2=$4
psrecord $(pgrep $pname1) --interval 1 --duration 60 --log $pname1.txt &
P1=$1
psrecord $(pgrep $pname2) --interval 1 --duration 60 --log $pname2.txt &
P2=$3
wait $P1 $P2
echo 'Done'

