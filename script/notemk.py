import os
join = os.path.join
exists = os.path.exists
from shutil import copyfile
from subprocess import check_output
import argparse
from notelib import get_notefiles, get_timestamp, get_root

NoteRoot = os.path.abspath("../")

def run():
    parser = argparse.ArgumentParser(description="notemk")
    parser.add_argument("tags", nargs='*')
    parser.add_argument("-n", "--name", default="note")
    args = parser.parse_args()
    notename = args.name
    build_dir = join(get_root(), "build", notename)
    
    interval = 1
    notefiles = get_notefiles(args.tags)            
    last = [0 for nf in notefiles]
    os.chdir(NoteRoot)

    if(not exists(build_dir)):
        os.makedirs(build_dir)
    copyfile(join(NoteRoot, "config/note.tex"),
             join(build_dir, "note.tex"))
    
    while True:
        check_output(["sleep", str(interval)])
        current = get_timestamp(notefiles)
        if(last!=current):
            check_output(["pandoc"] + notefiles +
                         ["-o", join(build_dir, "note_doc.tex")])
            os.chdir(build_dir)
            check_output(["latexmk", "note.tex"])
            os.chdir(NoteRoot)
            copyfile(join(build_dir, "note.pdf"),
                     join(NoteRoot, notename+".pdf"))
            last = current
        
run()
