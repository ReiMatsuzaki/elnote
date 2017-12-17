import os
join = os.path.join
from notelib import get_root, get_config
import argparse
import json

def run():
    json.load(open(join(get_config(), ))
    
    parser = argparse.ArgumentParser(description="notemk")
    parser.add_argument("tags", nargs='+')

    args = parser.parse_args()
    print args.tags

if __name__=='__main__':
    run()
    
