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

cmd_pandoc = ["pandoc", "--mathml", "-t", "html5"]

def run():
    parser = argparse.ArgumentParser(description="notemk")
    parser.add_argument("tags", nargs='*')
    parser.add_argument("-n", "--name", default="note")
    args = parser.parse_args()
    notename = args.name
    # dist_dir = join(get_root(), "dist", notename)
    dist_dir = join(get_root(), "dist")
    
    interval = 1
    notefiles = get_notefiles(args.tags)    
    
    last = [0 for nf in notefiles]
    os.chdir(NoteRoot)

    if(not exists(dist_dir)):
        os.makedirs(dist_dir)
    """
    copyfile(join(NoteRoot, "config/note.tex"),
             join(build_dir, "note.tex"))
    """
    
    while True:
        check_output(["sleep", str(interval)])
        current = get_timestamp(notefiles)
        if(last!=current):
            """
            for notefile in notefiles:
                cmd = ["sed", "s/\]\(fig/\]\("+os.path.dirname(notefile)+"\\/fig/g",
                       notefile]
                check_call(cmd, stdout=
            """
                
            cmd = cmd_pandoc + notefiles + [ "-o", join(dist_dir, notename+".html")]
            print
            print datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            print "update notebook."
            print "tags=", args.tags
            print "note:"
            for note in notefiles:
                print note
            
            try:
                check_output(cmd)
            except(Exception) as e:
                print "error"
                print e.message
            """
            cmd = ["pandoc"] + notefiles + ["-o", join(build_dir, "note_doc.tex")]
            print cmd
            check_call(cmd)
            os.chdir(build_dir)
            check_output(["latexmk", "note.tex"])
            os.chdir(NoteRoot)
            copyfile(join(build_dir, "note.pdf"),
                     join(NoteRoot, notename+".pdf"))
            """
            last = current
        
run()
