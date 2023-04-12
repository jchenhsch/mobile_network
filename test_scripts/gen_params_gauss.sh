#!/bin/bash
# The file is for the Gauss Markov model
declare -a num_nodes=("100")
declare -a range=("30"
                     "40"
                     "50"
                     "60"
                     "70"
                     "80"
                     "90"
                     "100"
                     "110"
                     "120")
declare -a avg_speed=(
                   "1"
                   "2"
                   "3")
declare -a sims=()
for ((i=0; i<${#num_nodes[@]}; i++))
do
    for ((k=0; k<${#avg_speed[@]}; k++))
    do
    for ((m=0; m<${#range[@]}; m++))
        do
        sims+=("${num_nodes[$i]} ${range[$m]} ${avg_speed[$k]}")
        #sims+=("${num_nodes[$i]} ${range[$m]}")
        done
    done
done
printf '%s\n' "${sims[@]}">>input_test.txt