#!/usr/bin/python
import os
join = os.path.join
exists = os.path.exists
from shutil import copyfile
from subprocess import check_call, check_output
import argparse
from datetime import datetime

from notelib import get_notefiles
import vt100

def run():
    parser = argparse.ArgumentParser(description="notemk")
    parser.add_argument("tags", nargs='*')
    parser.add_argument("-l", "--length", default=30)
    parser.add_argument("-n", "--num", type=int, default=0)
    parser.add_argument("-d", "--directory", action='store_true', default=False)
    parser.add_argument("--onlyheader", action='store_true', default=False)
    args = parser.parse_args()

    notefiles = get_notefiles(args.tags, range(-int(args.length),1))
    for note in notefiles:
        if(args.directory):
            # print os.dirname(note)
            print vt100.fg.GREEN + os.dirname(note) + vt100.END
        else:
            print vt100.fg.GREEN + note + vt100.END

        if(args.num!=0):
            with open(note, "r") as f:
                n = 0
                line = f.readline()                        
                while line:

                    skip = False
                    if(args.onlyheader):
                        if(("@" not in line) and ("#" not in line)):
                            skip = True

                    if(not skip):
                        if(line[0]=="#"):
                            print vt100.fg.YELLOW + line + vt100.END,
                        else:
                            print line,
                    
                    line =  f.readline()
                    n += 1
                    if(n==args.num):
                        break

                    """
                    if(line[0]!="#"):
                        print line,
                        n += 1
                    if(n == args.num):
                        break
                    """

if __name__=='__main__':
    run()
        
