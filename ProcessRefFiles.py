import os
##use ./sequence.fasta to work in the current directory.
Rfile = input("Enter a FASTA reference file: ")
Chr = input("What chromosome reference is this? (1-22, X, or Y): ")
Path = os.path.dirname(Rfile)
with open(Rfile, 'r') as rfileOG:
    head, tail = rfileOG.read().split('\n', 1)
with open(Rfile, 'w') as rfile:
    rfile.write(tail)
seq = ""
refseq = []
with open(Rfile,'r') as final:
    reflines = final.readlines()
    for line in reflines:
        refseq.append(line.strip())
    #combine all lines of reference sequence and convert to string
    seq = "".join(str(elem) for elem in refseq)

with open(Path + "/" + str(Chr) + ".FASTA",'w') as newfile:
    newfile.write(seq)
    newfile.close()



