
import sys
ebirdfile = open(sys.argv[1], encoding = "ISO-8859.15")
ebirddict = {}
ebirdfile.readline()

for row in ebirdfile:
    split = row.split(",")
    ebirddict[split[3]]=split[7]

for birdspecies in ebirddict:
    print("Species " + birdspecies + " belongs to Family " + ebirddict[birdspecies])
