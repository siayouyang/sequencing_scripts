#author: siayouyang
import os
from optparse import OptionParser

##OptionParser
parser = OptionParser()
parser.add_option("-i", "--input", dest="input", help="BED file obtained from plotHeatmap --outFileSortedRegions")
parser.add_option("-t", "--tss", dest="tss", help="TSS BED file")
(options, args) = parser.parse_args()

input = options.input
tss = options.tss

#cluster_1
heat_file = open(input, 'r')
heat_file_readlines = heat_file.readlines()
tss_file = open(tss, 'r')
tss_file_readlines = tss_file.readlines()
c1_file = open("c1_" + input, 'w')

for a in range(0, len(heat_file_readlines)):
    if str((heat_file_readlines[a]).split()[12]) == "cluster_1":
        for b in range(0, len(tss_file_readlines)):
            if str((heat_file_readlines[a]).split()[3]) == str((tss_file_readlines[b]).split()[3]) :
                c1_file.write(tss_file_readlines[b])
            else:
                pass
    else:
        pass
heat_file.close()
tss_file.close()
c1_file.close()

#cluster_2
heat_file = open(input, 'r')
heat_file_readlines = heat_file.readlines()
tss_file = open(tss, 'r')
tss_file_readlines = tss_file.readlines()
c2_file = open("c2_" + input, 'w')

for a in range(0, len(heat_file_readlines)):
    if str((heat_file_readlines[a]).split()[12]) == "cluster_2":
        for b in range(0, len(tss_file_readlines)):
            if str((heat_file_readlines[a]).split()[3]) == str((tss_file_readlines[b]).split()[3]) :
                c2_file.write(tss_file_readlines[b])
            else:
                pass
    else:
        pass
heat_file.close()
tss_file.close()
c2_file.close()

print("Done!")

