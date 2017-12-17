import os
exists = os.path.exists
from subprocess import check_output
from notelib import get_now

def run():
    interval = 100
    d = get_now()
    print d
    while True:
        check_output(["sleep", str(interval)])
        print 1
        if(not exists(d)):            
            print "make directory for today:", d
            os.makedirs(d)

run()

