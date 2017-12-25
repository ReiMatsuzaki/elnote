import os
join = os.path.join
exists = os.path.exists
expanduser = os.path.expanduser
import sys
import matplotlib as mpl
mpl.use('PDF')
import matplotlib.pylab as plt
import numpy as np
tr = np.transpose
import pandas as pd

def run():
    remote = "athena:~/Note/"
    local = expanduser("~/Note/")
    flag = "-avu"

    parser = argparse.ArgumentParser(description="sync")
    parser.add_argument("cmd")
    args = parser.parse_args()
    
    d = os.path.abspath(".")
    
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



