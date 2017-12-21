#!/usr/bin/python
import os
join = os.path.join
exists = os.path.exists
from shutil import copyfile
from subprocess import check_call, check_output
import argparse
import datetime
from notelib import get_notefiles
from datetime import datetime

def run():
    parser = argparse.ArgumentParser(description="notemk")
    parser.add_argument("tags", nargs='*')
    parser.add_argument("-l", "--length", default=5)
    parser.add_argument("-n", "--num", type=int, default=0)
    parser.add_argument("-d", "--directory", action='store_true', default=False)
    args = parser.parse_args()

    notefiles = get_notefiles(args.tags, range(-args.length,1))
    for note in notefiles:
        if(args.directory):
            print os.dirname(note)
        else:
            print note
            
        if(args.num!=0):
            with open(note, "r") as f:
                n = 0
                for nn in range(3*args.num):
                    line =  f.readline()
                    if(line[0]!="#"):
                        print line,
                        n += 1
                    if(n == args.num):
                        break
                print

if __name__=='__main__':
    run()
        
