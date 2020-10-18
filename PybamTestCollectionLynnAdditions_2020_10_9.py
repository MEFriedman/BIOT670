import pybam
from collections import namedtuple

# create collection format for each read
Read = namedtuple("Read", ["Name", "Chr", "Pos", "MAPQ",
                           "SuppAl", "ReadSeq", "ReadLen", "Cigar", "SA_Chr", "SA_Pos", "SA_MAPQ"])
# Do we still need SuppAl?
# create array to store read names (makes it easy to reference data in collections)
Reads = []

for alignment in pybam.read('ADAMC-PARK7.sam.sorted.bam'):
    # Lynn Stuff to parse SA string
    x = alignment.sam_tags_string
    x = x.split()[10]
    x = x.split(',')
    SA_chr = x[0].split("SA:Z:")[1]
    SA_pos = x[1]
    SA_MAPQ = int(x[4])

    # Joanna stuff
    if "SA:" not in alignment.sam_tags_string:  # filter out reads that do not have an alternate alignment
        continue
    # filter out reads with a MAPQ less than 50 OR SA_MAPQ less than 50
    if alignment.sam_mapq < 50 | SA_MAPQ < 50:
        continue
    else:
        # parses out the SA from sam_tags_string ***THIS NEEDS FURTHER PARSING: chr, position, MAPQ ***
        head, tail = alignment.sam_tags_string.split("SA:Z:")
        # create collection using Read tuple structure for each read
        x = Read(alignment.sam_qname, alignment.sam_rname, alignment.sam_pos1, alignment.sam_mapq,
                 tail, alignment.sam_seq, alignment.sam_l_seq, alignment.sam_cigar_string, SA_chr, SA_pos, SA_MAPQ)
        # Lynn stuff added on the end of the Read
        # append each collection to an array (stores them all in one list, while maintaining collection structure)
        Reads.append(x)

# sort alphabetically by read name
Reads.sort()

# example of pulling pieces of data from collections
# print(Reads[1].Chr)
# print(Reads[1].Pos)
# print(Reads[1].MAPQ)

print(Reads[1])

# read into reference sequence
# refFile = open(r"C:/transit/Project/GRCh38_Chr1.fasta")
# refLines = refFile.readlines()
# seq = ""
# refseq = []
# #****I WANT TO REDO THIS AS A COLLECTION WITH THE NAME AND SEQUENCE STORED FOR EACH CHROMOSOME****
# for line in refLines:
#     #store name of reference from line containing ">"
#     if line.startswith(">"):
#         refname = line.strip(">")
#         continue
#     #append sequence lines to array and strip /n
#     else:
#         refseq.append(line.strip())

# #combine all lines of reference sequence and convert to string
# seq = "".join(str(elem) for elem in refseq)

# #printing some random information from the read collections
# for i in Reads:
#     print("Read: ", i.Name)
#     print("Alignment Location: ", i.Chr, i.Pos)
#     print("Supplementary Alignment: ",i.SuppAl)
#     print("Read Length: ", i.ReadLen)
#     print("Cigar:", i.Cigar)
#     print("Read Seq:", i.ReadSeq)
#     #this uses the chromosome position and read length for each read to pull that segment from the reference file by simple character count
#     print("Ref Seq: ", seq[(i.Pos - 1):(i.Pos + i.ReadLen - 1)])
#     print("")

# #prints example of what a collection for each read looks like
# print(Reads[1])
