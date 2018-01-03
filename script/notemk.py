import sys
import os
join = os.path.join
exists = os.path.exists
from shutil import copyfile
from subprocess import check_call, check_output
import argparse
import datetime
from notelib import get_notefiles, get_timestamp, get_root

NoteRoot = os.path.abspath("../")
from datetime import datetime

cmd_pandoc = ["pandoc", "--mathml", "-t", "html5", "-c", join(NoteRoot, "config/github.css"), "--metadata", "title=note", "-s"]
cmd_reload = ["osascript", join(NoteRoot, "script", "reload_safari.scpt")]
#cmd_pandoc = ["pandoc", "--mathjax=script/dynoload.js","-t", "html5"]

def run():
    parser = argparse.ArgumentParser(description="notemk")
    parser.add_argument("tags", nargs='*')
    parser.add_argument("-n", "--name", default="note")
    parser.add_argument("-l", "--length", default=30)
    args = parser.parse_args()
    notename = args.name
    dist_dir  = join(get_root(), "dist")

    if(not exists(dist_dir)):
        os.makedirs(dist_dir)
    
    interval = 1
    notefiles = get_notefiles(args.tags, range(-int(args.length),1))
    modfiles  = [f+".md" for f in notefiles]
    
    last = [0 for nf in notefiles]
    os.chdir(NoteRoot)
    
    """
    copyfile(join(NoteRoot, "config/note.tex"),
             join(build_dir, "note.tex"))
    """
    
    while True:
        check_output(["sleep", str(interval)])
        current = get_timestamp(notefiles)
        if(last!=current):

            for i in range(len(notefiles)):
                if(last[i]!=current[i]):
                    d = os.path.dirname(notefiles[i])
                    fi = open(notefiles[i], "r")
                    fo = open(modfiles[i], "w")
                    lines = fi.read()
                    lines = lines.replace("fig", d+"/fig")
                    fo.write(lines)
                    fi.close()
                    fo.close()
                    print
                    print datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                    print "update notebook."
                    print "tags=", args.tags
                    print "note:", notefiles[i]
 
            cmd = cmd_pandoc + modfiles + [ "-o", join(dist_dir, notename+".html")]
            print ""
            print datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            print "pandoc begin"
            try:
                check_output(cmd)
                check_output(cmd_reload)
            except(Exception) as e:
                print "error"                
                print e.message
                sys.exit("stop notemk.py ...")

            print "pandoc end"
            last = current
        
run()
