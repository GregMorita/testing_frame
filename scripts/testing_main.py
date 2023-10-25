import subprocess
import sys
import glob
import getopt

options = "hrv:"
arglst = sys.argv[1:]
opt = ""
val = False

"""
Simple python script to help test c code
compiles and runs code on a test dir
by default, takes stdout of program on testfile and diffs with expected
requires installation of gcc, python 3, and valgrind
"""

#compiles program with all warnings
def compile(program: str):
    subprocess.run(["gcc -Wall -pedantic -std=c99", program, "-g"])

#tests for mem leaks
def valgrind(program: str, args: list):
    pass

def parsing_args():
    if (len(sys.argv) < 4 and len(sys.argv) > 2):
        print("improper amount of arguments, try testing.py -h")
    
    try:
        arguments = getopt.getopt(arglst, options) #TODO: read up on getopt.py

        for currentArgument in arguments:
    
            if currentArgument in ("-h"):
                print("Usage: testing.py Testcase_dir Testcase_ans_dir Program_path [Program_args] [-hrv]")
                print("r: runs files in Testcase_dir, passes in Testcase_ans_dir filepath for use on smaller, incremental tests") 
                print("h: displays this message. v: runs valgrind on program to check for memLeaks")
                exit(0)

            elif currentArgument in ("-r"):
                opt = "r"
            
            elif currentArgument in ("-v"):
                val = True
            
    except getopt.error as err:
        print(str(err))

def main(): 
    
    total_args = len(sys.argv[0])

    #just a lil' bit fucked
    if val:
        valgrind()
    else:
        compile(prog)

    subprocess.run([])


if (__name__ == '__main__'):
    main()