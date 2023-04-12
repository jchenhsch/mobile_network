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
declare -a mean_speed=(
                   "1"
                   "2"
                   "3")
declare -a turn_prob=("0.1"
                    "0.3"
                    "0.5"
                    "0.7"
                    "0.9")
declare -a sims=()

for ((i=0; i<${#num_nodes[@]}; i++))
do
    for ((k=0; k<${#mean_speed[@]}; k++))
    do
    for ((m=0; m<${#range[@]}; m++))
        do
        for ((n=0; n<${#turn_prob[@]}; n++))
            do
            sims+=("${num_nodes[$i]} ${range[$m]} ${mean_speed[$k]} ${turn_prob[$n]}")
            done
        done
    done
done
printf '%s\n' "${sims[@]}">>input_test.txt