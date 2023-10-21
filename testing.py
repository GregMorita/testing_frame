import subprocess
import sys
import glob
import getopt
import typing

options = "rhv:"
arglst = sys.argv[1:]
opt = ""

"""
Simple python script to help test c code
compiles and runs code on a test dir
by default, takes stdout of program on testfile and diffs with expected
"""

def compile(program: str):
    subprocess.run(["gcc -Wall -pedantic -std=c99", program, "-g"])

def valgrind(program: str, args: list):
    pass

def main(): 
    if (len(sys.argv) < 3):
        print("improper amount of arguments, try testing.py -h")
    
    try:
        arguments = getopt.getopt(arglst, options)

        for currentArgument in arguments:
    
            if currentArgument in ("-h"):
                print("Usage: testing.py [-r Testing_dir] [-hv] [program args] Program_path Test_case_dir Testcase_answer_dir ")
                print("r: runs files in Testing_dir, passes in testdir filepath use for smaller, incremental tests") 
                print("h: displays this message")
                exit(0)

            elif currentArgument in ("-r"):
                opt = "r"
            
            elif currentArgument in ("-v"):
                val = True
            
    except getopt.error as err:
        print(str(err))
    
    total_args = len(sys.argv[0])
    prog = sys.argv[total_args - 3]
    #just a lil' bit fucked
    if val:
        pass
    else:
        compile(prog)

    for file in glob.glob('*.txt'):
        subprocess.run(["./a.out", file, "| diff", file + ".soln"])


if (__name__ == '__main__'):
    main()