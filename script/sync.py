import os
join = os.path.join
exists = os.path.exists
expanduser = os.path.expanduser
from subprocess import check_call
import argparse
from notelib import get_dirs

def run():    
    remote = "portia:/home/matsuzaki/Note/"
    local = expanduser("~/Note/")
    flag = "-av"

    parser = argparse.ArgumentParser(description="sync")
    parser.add_argument("cmd")
    args = parser.parse_args()
    
    ds = get_dirs([-1, 0], use_abs=False)
    for d in ds:
        l = local+d + "/"
        r = remote+d + "/"
        if(not exists(l)):
            os.makedirs(l)
        if(args.cmd=="push"):
            cmd = ["rsync", flag, l, r]
        elif(args.cmd=="pull"):
            cmd = ["rsync", flag, r, l]
        else:
            raise RuntimeError("unsupported")
        print cmd
        check_call(cmd)

if __name__=='__main__':
    run()

    
