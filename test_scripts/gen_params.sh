#!/bin/bash

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
declare -a mean_speed=( 
                   "1"
                   "2"
                   "3")
declare -a sims=()

for ((i=0; i<${#num_nodes[@]}; i++))
do
    for ((k=0; k<${#mean_speed[@]}; k++))
    do
    for ((m=0; m<${#range[@]}; m++))
        do
        sims+=("${num_nodes[$i]} ${range[$m]} ${mean_speed[$k]}")
        done
    done
done
printf '%s\n' "${sims[@]}">>input_test.txt