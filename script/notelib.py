import os
join = os.path.join
exists = os.path.exists
from subprocess import check_output
import datetime
import json

def get_root():
    return os.path.expanduser("~/Note")

def get_config():
    return join(get_root(), "config")

def get_dirs(days):
    d0 = datetime.date.today()
    res = []
    for dd in days:
        dt = d0+datetime.timedelta(dd)
        y = dt.year
        m = dt.month
        d = dt.day
        res.append(join(get_root(), "daily", str(y), str(m), str(d)))
    return res

def get_notefiles(tags=None, days=None):
    
    if days is None:
        notejson = join(get_config(), "note.json")
        j = json.load(open(notejson))
        len_day = j["len_day"]
        days = range(-len_day, 0+1)
    
    note_list = []
    for dir_day in get_dirs(days):
        if(exists(dir_day)):
            for dd in os.listdir(dir_day):
                d = join(dir_day, dd)
                with open(join(d, "TAG")) as f:
                    tags0 = f.read().split()
                if(tags is None):
                    note_list.append(join(d, "note.org"))
                elif(all([(t in tags0) for t in tags])):
                    note_list.append(join(d, "note.md"))
    return note_list

def get_timestamp(files):
    return [
        check_output(["openssl", "sha256", "-r", f]).split()[0]        
        for f in files]

if __name__=='__main__':
    #print get_dirs([-2,1,0])
    print get_notefiles(["lif"])


