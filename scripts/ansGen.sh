#!/bin/sh
PROG=something
COUNT=0

for DIR in ./*_tests
do
    echo this is $DIR:
    for file in ${DIR}/t*
    do 
        expr $COUNT + 1
        echo $file
    done
done

