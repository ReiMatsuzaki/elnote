import os
exists = os.path.exists
from subprocess import check_output
from notelib import get_dirs

def run():
    interval = 1
    d = get_dirs([0])[0]
    while True:
        check_output(["sleep", str(interval)])
        if(not exists(d)):            
            print "make directory for today:", d
            os.makedirs(d)

run()

