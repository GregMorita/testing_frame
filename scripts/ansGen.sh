#!/bin/sh
COUNT=0

# uses $1 for the program to be used

for DIR in ./*tests
do
    if [ ! -d $DIR ]; then
        echo "testing directory doesn't exist"
        exit
    fi

    echo this is $DIR:
    for file in ${DIR}/*.txt
    do 
        echo $file
    done
done

