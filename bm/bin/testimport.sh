#! /bin/sh


filename='IRP.irp'
n=1
while read line; do
	#echo "Line No. $n : $line"
        #str=$( $line | sed 's/.*\[\([^]]*\)\].*/\1/g')
        #str=`$line | awk -vRS="]" -vFS="[" '{print $2}'`echo $line | awk -vRS="]" -vFS="[" '{print $2}'
        #str=`$line | awk -vRS="]" -vFS="[" '{print $2}'`
        #str=`$line|awk-vRS="]"-vFS="["'{print $2}'`
        echo $line | awk -vRS="]" -vFS="[" '{print $2}'
	#echo $str
	n=$((n+1))
       # break
done < $filename
