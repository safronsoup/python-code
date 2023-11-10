# basic parameters that print() can accept:
# 1. object - the thing(s) to be printed
# 2. sep - how to separate the instance of multiple object
# 3. end - what to print at the end
# 4. file - redirect to a file on the file system

# write output to file output.txt; mode = w means write (overwrite what is already there)
fileObject = open("output.txt", mode="w")

# print("Hello there!", file=fileObject)

# print("Hello", "Jeff", "ThirdValue", file=fileObject, sep = ":")

# print("Hello", file=fileObject, end=" ")
# print("Goodbye", file=fileObject)

BEGIN = ""
END = ""
CCSD = "MAB2"
HOSTNAME = "UCEEPTM010"
TYPE = "ETH"
BW = "1G"
ROUTING = "ISIS"
INACL = "LINE-INGRESS"
OUTACL = "LINE-EGRESS"
DEIP = "142.17.1.2"
COMMENT = "MEDIA-CONVERTERS-ON-CIRCUIT"

print(BEGIN, CCSD, HOSTNAME, TYPE, BW, ROUTING, INACL, OUTACL, DEIP, COMMENT, END, sep = "::", file=fileObject)
