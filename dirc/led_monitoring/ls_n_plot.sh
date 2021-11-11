#!/bin/bash

# for z in `echo hist_Run*`
# do
# root -b -q timing_plot.C\(\"$z\"\)
# done

#root -b -q timing_plot.C\(\"hd_root_071370.root\"\)

rm aaa
touch aaa

#$LED_north_variation("$z")

#llls=".ls"

#$llls
#export zzzz=hd_root_071370.root

#echo $zzzz

for z in `echo hd_root_*`
do
export zzzz=$z
root -l <<'EOF' | grep -v TString >> aaa
TString file_name = gSystem->GetFromPipe("echo $zzzz")
.L LED_variation.C
LED_north_variation(file_name)
EOF
done

#.L LED_variation.C
#LED_north_variation(file_name)

# for z in `echo hd_root_*`
# do
# root -l <<'EOF' | grep "^  " >> aaa
# TString asd = gSystem->GetFromPipe("echo  ")
# EOF
# done


# i=1
# val1=beep
# val2=bop
# 
# rightval="val$i"
# cat <<EOF
# This is a beep: ${!rightval}
# EOF
