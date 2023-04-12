#!/bin/bash

#call directly after cd or use call_bm.sh at home directory (executable)
#cd Desktop/Senior\ thesis/test_scripts > /dev/null


rm -r input*.txt > /dev/null
bash ./gen_params.sh
echo "*" >> input_test.txt
bash ./gen_params_gauss.sh
echo "**" >> input_test.txt
bash ./gen_params_manhattan.sh

dirname_rand='SteadyStateRandomWaypointScenarios1'
dirname_org_gauss='OriginalGaussMarkovScenario1'
dirname_manhattan="ManhattanGridScenario1"

dirname_rand_out='SteadyStateRandomWaypointScenario1_CSV'
dirname_org_gauss_out='OriginalGaussMarkovScenario1_CSV'
dirname_manhattan_out="ManhattanGridScenario1_CSV"
outpicdirname="plotoutput"

#declare -a interval=(5 10)

flag_org=0
flag_man=0
timestep=1.0

sudo rm -r $dirname_rand > /dev/null
sudo rm -r $dirname_org_gauss > /dev/null
sudo rm -r $dirname_manhattan > /dev/null
sudo rm -r $dirname_rand_out > /dev/null
sudo rm -r $dirname_org_gauss_out > /dev/null
sudo rm -r $dirname_manhattan_out > /dev/null

mkdir $dirname_rand
mkdir $dirname_org_gauss
mkdir $dirname_manhattan

mkdir $outpicdirname
mkdir $dirname_manhattan_out
mkdir $dirname_org_gauss_out
mkdir $dirname_rand_out
cat input_test.txt | while read line 
do  
    if [ "$line" = "*" ];
    then
        #echo "$line"
        flag_org=1
        continue
    elif [ "$line" = "**" ];
    then
       #echo "$line"
       flag_man=1
       continue
    fi
       
    if [ $flag_org -eq 0 ];
    then
       #echo "rand, here $line"
       IFS=" " read -a myarray <<< $line
       node_num=${myarray[0]}
       range=${myarray[1]}
       mean_speed=${myarray[2]}
       filename="${line// /_}"
       /Users/james/Desktop/Senior\ thesis/bm/bin/bm  -f $dirname_rand/$filename SteadyStateRandomWaypoint -n $node_num -d 10 -i 3600 -x 500 -y 500 -o $mean_speed > /dev/null
       /Users/james/Desktop/Senior\ thesis/bm/bin/bm InRangePrinter -f $dirname_rand/$filename -n $node_num -l $timestep -r $range > /dev/null
       sed 's/\[//g; s/\]//g' $dirname_rand/$filename.irp >> $dirname_rand/$filename.txt
       python parse_output.py $dirname_rand/$filename.txt $node_num $range SteadyStateRandomWaypoint_$filename.csv > /dev/null

    #elif [ 0 ];
    elif [ $flag_org -eq 1 ] && [ $flag_man -eq 0 ];
    then
       #echo "org, here $line"
       IFS=" " read -a myarray <<< $line
       node_num=${myarray[0]}
       range=${myarray[1]}
       avg_speed=${myarray[2]}
       filename="${line// /_}"
       ~/Desktop/Senior\ thesis/bm/bin/bm  -f $dirname_org_gauss/$filename OriginalGaussMarkov -n $node_num -d 10 -i 3600 -x 500 -y 500 -a $avg_speed -w 0.3 -s 0.5 -q 30 > /dev/null
       ~/Desktop/Senior\ thesis/bm/bin/bm InRangePrinter -f $dirname_org_gauss/$filename -n $node_num -l $timestep -r $range > /dev/null
       sed 's/\[//g; s/\]//g' $dirname_org_gauss/$filename.irp >> $dirname_org_gauss/$filename.txt
       python parse_output.py $dirname_org_gauss/$filename.txt $node_num $range OriginalGaussMarkov_$filename.csv > /dev/null
    else
       #echo "manhatten, here $line"
       IFS=" " read -a myarray <<< $line
       node_num=${myarray[0]}
       range=${myarray[1]}
       mean_speed=${myarray[2]}
       turn_prob=${myarray[3]}
       #echo "here, $turn_prob"
       filename="${line// /_}"
       ~/Desktop/Senior\ thesis/bm/bin/bm -f $dirname_manhattan/$filename ManhattanGrid -n $node_num -d 10 -i 3600 -x 500 -y 500 -o 0 -c 0.3 -m $mean_speed -s 0.5 -t $turn_prob > /dev/null
       ~/Desktop/Senior\ thesis/bm/bin/bm InRangePrinter -f $dirname_manhattan/$filename -n $node_num -l $timestep -r $range > /dev/null
       sed 's/\[//g; s/\]//g' $dirname_manhattan/$filename.irp >> $dirname_manhattan/$filename.txt
       python parse_output.py $dirname_manhattan/$filename.txt $node_num $range ManhattanGrid_$filename.csv > /dev/null
    fi

    
    #python bm_networkx.py $filename.csv $node_num > /dev/null
    
    #/Users/james/Desktop/Senior\ thesis/bm/bin/bm CSVFile  -f $dirname/$filename.    

    # echo $node_num
    # echo $duration
    # echo ${#myarray[@]}
done

mv SteadyStateRandomWaypoint*.csv ./$dirname_rand_out
mv OriginalGaussMarkov*.csv ./$dirname_org_gauss_out
mv ManhattanGrid*.csv ./$dirname_manhattan_out


python plot_metric.py $dirname_rand_out SteadyStateRandomWaypoint #$interval
python plot_metric.py $dirname_org_gauss_out OriginalGaussMarkov #$interval
python plot_metric.py $dirname_manhattan_out ManhattanGrid #$interval

mv *.png ./$outpicdirname

#find $dirname/$filename.irp -exec sed 's/\[//g' {} \; >> $dirname/$filename.irp
# find $dirname/$filename.irp -exec sed 's/\]//g' {} \; >> $dirname/$filename.csv