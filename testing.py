import subprocess
import sys
import glob
import getopt

options = "rhv:"
arglst = sys.argv[1:]
opt = ""

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

def main(): 
    if (len(sys.argv) < 4 and len(sys.argv) > 2):
        print("improper amount of arguments, try testing.py -h")
    
    try:
        arguments = getopt.getopt(arglst, options)

        for currentArgument in arguments:
    
            if currentArgument in ("-h"):
                print("Usage: testing.py [-hvr] Testcase_dir Testcase_ans_dir Program_path [Program_args]")
                print("r: runs files in Testcase_dir, passes in Testcase_ans_dir filepath for use on smaller, incremental tests") 
                print("h: displays this message. v: runs valgrind on program to check for memLeaks")
                exit(0)

            elif currentArgument in ("-r"):
                opt = "r"
            
            elif currentArgument in ("-v"):
                val = True
            
    except getopt.error as err:
        print(str(err))
    
    total_args = len(sys.argv[0])

    #just a lil' bit fucked
    if val:
        valgrind()
    else:
        compile(prog)

    for file in glob.glob('*.txt'):
        subprocess.run(["./a.out", file, "| diff", file + ".soln"])


if (__name__ == '__main__'):
    main()