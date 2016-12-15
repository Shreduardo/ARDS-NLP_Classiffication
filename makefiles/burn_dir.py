import sys, pandas, string, numpy
import csv
import re
import codecs
import pprint
import os
sys.dont_write_bytecode = True

base = '/home/shared/'
yesCsv = base + 'ards/data/burn_yes.csv'
noCsv = base + 'ards/data/burn_no.csv'
data = base + 'ards/data/burn_notes_09282016.txt'
out = base + 'ards/text1'
diagCsv = noCsv = base + 'ards/data/diags.csv'

def get_diags():
        # create diags.csv mapping MRN to ARDS status
        diags = []
        cnt = 0

        with open(yesCsv) as f:
                cfo = csv.reader(f, delimiter=',')

                for row in cfo:

                        diags.append([row[6], 'Yes'])
                        cnt += 1

        with open(noCsv) as f:
                cfo = csv.reader(f, delimiter=',')

                for row in cfo:

                        diags.append([row[6], 'No'])
                        cnt += 1

        with open(diagCsv, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(diags)
        print('read ' + str(cnt) + ' diags')


def get_notes():
        # read the MRN and notes columns into a dict 
        notes = []

        with codecs.open(data, 'r', encoding='utf-8', errors='ignore')as f:
                for row in f:
                        temp = (row.split('||'))
                        notes.append([temp[0], temp[8]])
        print('num notes: ' + str(len(notes)))
        return notes


def join():
        # create dir structure of notes named by MRN and categorized by diagnosis
        j_stuff = []
        diags = {}
        cnt = 0
        err = 0

        get_diags()

        notes = get_notes()

        with open(diagCsv) as infile:
                cfo = csv.reader(infile)

                for row in cfo:
                        diags[row[0]] = row[1]

        for note in notes:

                if note[0] == 'mrn':
                        continue
                cnt += 1

                try:
                        name = base + 'ards/text1/' + diags[note[0]] + '/' + note[0] + '.txt'
                        print(name)
                        with open(base + 'ards/text1/' + diags[note[0]] + '/' + note[0] + '.txt', 'a') as f:
                                f.write(note[1])

                except Exception as e:
                        err += 1

        print('total written: ' + str(cnt) + ' total errors: ' + str(err))

if __name__ == "__main__":
   join()


