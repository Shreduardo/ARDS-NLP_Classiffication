
import os, string, re

#Replace dummy with final for the official clean
directory = '/home/shared/ards/Jtest_text_clean'
write_directory = '/home/shared/ards/Jtest_text_clean2'
stoppath = ''
def remPunc(str):
    try:
        return re.sub(r'[^\w\s]',' ',str)
    except ValueError:
        return str

def remNumber(str):
    try:
        return re.sub(" \d+", " ", str)
    except ValueError:
        return str

def remExtraSpace(str):
    try:
        return re.sub(' +',' ',str)
    except ValueError:
        return str
def get_just_file (filepath):
    opened = []
    with open(filepath, 'r') as f:
        for line in f:
            for word in line.split():
                opened.append(word.lower())
    return opened
def get_file(filepath):
    opened =[]
    with open(filepath,'r') as f:
        for line in f:
            line = remPunc(line)
            line = remNumber(line)
            line = remExtraSpace(line)
            for word in line.split():
                word = remExtraSpace(word)
                word = remNumber(word)
                word = remExtraSpace(word)
                opened.append(word.lower())
    return opened
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def straight_join():
    stopwords = get_just_file(stoppath + "StopWords.txt")
    for subdir, dirs, files in os.walk(directory):
        diag_directory = subdir.split("/")
        for f in files:
            notes = get_file(subdir+"/" + f)
            strNotes = " ".join([word for word in notes if not word in stopwords])
            strNotes = remExtraSpace(strNotes)
            with open(write_directory + "/" + diag_directory[-1]+"/"+f,'w') as q:
                q.write(strNotes)
def clean_dir():
    stopwords = get_just_file(stoppath + "StopWords.txt")

    for subdir, dirs, files in os.walk(directory):
        diag_directory = subdir.split("/")
        for f in files:
            notes = get_file(subdir+ "/" + f)
            for w in notes:
                if len(w.replace(" ","")) < 3:
                    notes.remove(w)
                elif len(w) < 3:
                    notes.remove(w)
                elif RepresentsInt(w):
                    notes.remove(w)
                elif w in stopwords:
                    notes.remove(w)
            notes = " ".join(x for x in notes)
            notes = remExtraSpace(notes)
            with open(write_directory + "/" + diag_directory[-1] + "/" + f, 'w') as q:
                q.write(notes)
#clean_dir()
straight_join()
