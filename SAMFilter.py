#author: siayouyang
#default is to include 130bp-180bp nucleosome DNA fragments and exclude repetitive rRNA locus(chrXII:451275-469084)
from optparse import OptionParser

##OptionParser
parser = OptionParser()
parser.add_option("-i", "--input",dest="input", help="input data in SAM format(from Bowtie2)")
parser.add_option("-c","--chr", dest="chr", type="str", default="chrXII",help="chromosome of the region to be excluded. Default %default")
parser.add_option("-s", "--start", dest="start", type="int", default=451275, help="start of the region to be excluded. Default %default.")
parser.add_option("-e", "--end", dest="end", type="int", default=469084, help="end of the region to be excluded. Default %default.")
parser.add_option("--minLength", dest="minLength", type="int", default=130, help="minimum fragment length. Default %default.")
parser.add_option("--maxLength", dest="maxLength", type="int", default=180, help="maximum fragment length. Default %default.")
parser.add_option("-o", "--output",dest="output", help="output file name")
(options, args) = parser.parse_args()

input = options.input
chr = options.chr
start = int(options.start)
end = int(options.end)
minLength = int(options.minLength)
maxLength = int(options.maxLength)
output = options.output

input_file = open(input, 'r')
input_file_readlines = input_file.readlines()
output_file = open(output , 'w')
for a in range(0, len(input_file_readlines)):
    if (str(input_file_readlines[a].split()[0]) == "HD") or (str(input_file_readlines[a].split()[0]) == "SQ") or (str(input_file_readlines[a].split()[0]) == "PG"):
        output_file.write(input_file_readlines[a])
        continue
    elif ((str(input_file_readlines[a].split()[2])) == chr) and ((int(input_file_readlines[a].split()[3])) >= start) and ((int(input_file_readlines[a].split()[3])) <= end) and ((int(input_file_readlines[a].split()[7])) >= start) and ((int(input_file_readlines[a].split()[7])) <= end):
        continue
    elif (abs(int(input_file_readlines[a].split()[8])) < minLength) or (abs(int(input_file_readlines[a].split()[8])) > maxLength):
        continue
    else:
        output_file.write(input_file_readlines[a])
input_file.close()
output_file.close()

print("Done!")


