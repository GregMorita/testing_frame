#!/bin/sh

touching()
{
    for i in 1 2 3 4 5 6 7 8 9
    do
        WORD=t${i}.txt
        touch $WORD
        echo created $WORD
        mv ${WORD} ${1}
        echo moved $WORD to $1
    done
}

for DIR in ./*_tests
do
    if [ ! -d $DIR ]
    then
        echo "doesn't exists, creating dir: ./tests"
        mkdir ./tests
        touching ./tests

    else
        touching $DIR
    fi
done