# Parser for 2g rbs hw to *.txt

# Working version


# ****** OSS Script *******

# rxmop:moty=rxotg;
# rxmop:moty=rxotrx;
# rxmfp:moty=rxotrx;

# **************************

import time
start_time = time.time()

# open files
inputFile = open("rbs_hw_input.txt", "r")
outputFile = open("output.txt", "w")

# set variables
BSC = ""
TG = ""
RSITE = ""
RXOTRX = ""
BSC_TG = ""
MODE = ""
CELL = ""
SIG = ""
TG = ""
RUREVISION = ""
RUSERIALNO = ""
ind1 = 0
ind2 = 0
ind3 = 0
RXOTRX_in_array3 = ""
RXOTRX_in_array2 = ""
BSC_TG_in_array2 = ""
BSC_TG_in_array1 = ""

main_header = "BSC_RXOTRX1,BSC_TG1,RXOTRX,RUREVISION,RUSERIALNO,BSC_RXOTRX2,BSC_TG2,BSC,TG,CELL,SIG,BSC_TG3,RSITE," + "\n"

# set arrays
array1 = []
array2 = []
array3 = []

# write header to output file
outputFile.write(main_header)

# main loop over entire file
for line in inputFile:  # read line by line from file

    # read bsc header
    if line.find("Connected to ") != -1:
        BSC = line[17:25].strip()

        # check MODE
    if line.find("RXMOP:MOTY=RXOTG") != -1:  # trigger rxmop:moty=rxotg block
        MODE = "rxmop_rxotg"
    elif line.find("RXMOP:MOTY=RXOTRX") != -1:  # trigger rxmop_rxotrx block'
        MODE = "rxmop_rxotrx"
    elif line.find("RXMFP:MOTY=RXOTRX") != -1:  # trigger rxmfp_rxotrx block'
        MODE = "rxmfp_rxotrx"

    # loop for MODE = rxmop_rxotg
    if MODE == "rxmop_rxotg":
        if line.find("RXOTG-") != -1:
            TG = line[6:17]
            RSITE = line[18:53].strip()
            BSC_TG = BSC + "_" + TG
            BSC_TG = BSC_TG.ljust(15)
            array1.append(BSC_TG + "," + RSITE)

    # loop for MODE = rxmop_rxotrx
    if MODE == "rxmop_rxotrx":
        if line.find("RXOTRX-") != -1:
            RXOTRX = line[0:17]
            CELL = line[18:24].strip()
            SIG = line[45:53].strip()
            TG = RXOTRX[7:RXOTRX.rfind('-')]
            BSC_TG = BSC + "_" + TG
            BSC_TG = BSC_TG.ljust(15)
            BSC_RXOTRX = BSC + "_" + RXOTRX
            array2.append(BSC_RXOTRX + "," + BSC_TG + "," + BSC + "," + TG + "," + CELL + "," + SIG)

    # loop for MODE = rxmfp_rxotrx
    if MODE == "rxmfp_rxotrx":
        if line.find("RXOTRX-") != -1:
            RXOTRX = line[0:17]
            TG = RXOTRX[7:RXOTRX.rfind('-')]
        # find RXOTRX block
        if line.find(" 0  KRC ") != -1:  # find string wth codec name
            RUREVISION = line[4:25].strip()
            RUSERIALNO = line[41:53].strip()
            BSC_TG = BSC + "_" + TG
            BSC_TG = BSC_TG.ljust(15)
            BSC_RXOTRX = BSC + "_" + RXOTRX
            array3.append(BSC_RXOTRX + "," + BSC_TG + "," + RXOTRX + "," + RUREVISION + "," + RUSERIALNO)

    if line.find("Disconnected") != -1:
        # get three arrays together

        for row_array3 in array3:
            RXOTRX_in_array3 = row_array3[0:24]
            BSC_TG_in_array3 = row_array3[26:40]
            for row_array2 in array2:
                RXOTRX_in_array2 = row_array2[0:24]
                if RXOTRX_in_array3 == RXOTRX_in_array2:
                    for row_array1 in array1:
                        BSC_TG_in_array1 = row_array1[0:14]
                        if BSC_TG_in_array3 == BSC_TG_in_array1:
                            outputFile.write(row_array3 + "," + row_array2 + "," + row_array1 + "\n")
                    #         array3.remove(row_array3)
                    # array2.remove(row_array2)

        # clear caches
        array1.clear()
        array2.clear()
        array3.clear()
        print(line)

        # your lists have DIFFERENT sizes, so parser works incorrect or input data is incorrect or both
        # print(len(array1))
        # print(len(array2))
        # print(len(array3))


# for i in range(len(array1)):
#    outputFile.write (array1[i] + "\n")

# for i in range(len(array2)):
#    outputFile.write (array2[i] + "\n")

# for i in range(len(array3)):
#    outputFile.write (array3[i] + "\n")




inputFile.close
outputFile.close
print("--- %s seconds ---" % (time.time() - start_time))