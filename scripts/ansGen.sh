#!/bin/sh
COUNT=0

# uses $1 for the program to be used

if [ $# -gt 0 ]; then
    for DIR in ./*tests
    do
        if [ ! -d $DIR ]; then
            echo "testing directory doesn't exist"
            exit
        fi

        echo this is $DIR:
        for file in ${DIR}/*.txt
        do 
            SUFF=".txt"
            ANS=${file%"$SUFF"}_ans.txt
            touch ${ANS}
            $1 $file >> $ANS
        done
    done
fi
