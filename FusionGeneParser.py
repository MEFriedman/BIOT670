import pybam
from collections import namedtuple

#create collection format for each read
Read = namedtuple("Read",["Name","Chr","Pos","SuppAl","ReadSeq","ReadLen","Cigar","SA_Chr", "SA_Pos", "SA_MAPQ"])

#create array to store read names (makes it easy to reference data in collections)
Reads = []

for alignment in pybam.read('./ADAMC-PARK7.sam.sorted.bam'):
    #parses out the SA from sam_tags_string ***THIS NEEDS FURTHER PARSING: chr, position, MAPQ ***
    head, tail = alignment.sam_tags_string.split("SA:Z:")
    x = tail.split(',')
    SA_chr = x[0]
    SA_pos = x[1]
    SA_MAPQ = int(x[4])
    if "SA:" not in alignment.sam_tags_string: #filter out reads that do not have an alternate alignment
        continue
    if alignment.sam_mapq <50 | SA_MAPQ < 50: #filter out reads with a MAPQ less than 50
        continue
    else:
        #create collection using Read tuple structure for each read
        chro = alignment.sam_rname.strip("chr")
        x = Read(alignment.sam_qname,chro,alignment.sam_pos1,tail,alignment.sam_seq,alignment.sam_l_seq,alignment.sam_cigar_string,SA_chr,SA_pos,SA_MAPQ)
        #append each collection to an array (stores them all in one list, while maintaining collection structure)
        Reads.append(x)

#sort alphabetically by read name
Reads.sort()

#printing some random information from the read collections
for i in Reads:
    Rfilename = "./" + str(i.Chr) + ".FASTA"
    Rfile = open(Rfilename,'r')
    Rfile.read(i.Pos - 1)
    print("Read: ", i.Name)
    print("Alignment Location: ", i.Chr, i.Pos)
    print("Supplementary Alignment: ",i.SuppAl)
    print("Read Length: ", i.ReadLen)
    print("Cigar:", i.Cigar)
    print("Read Seq:", i.ReadSeq)
    print("Ref Seq: ", Rfile.read(i.ReadLen))
    print("")





