inputFile = open("dip_state.txt", "r")
outputFile = open("output.txt", "w")
array = inputFile.readlines()
findhead = 0
SDIP = ""
SNT = ""
MS = ""
MAINDATA = ""
SDIPP = 6

listTpcop = []
listDtstp = []
# mode 1 for tpcop, 2 fot dtstp
mode = 1
for s in array:

    if s.find("<tpcop") != -1:
        mode = 1
    elif s.find("<dtstp") != -1:
        mode = 2

    if mode == 1:
        # work with string after header
        if findhead == 1:
            findhead = 0
            SDIP = s[0:8]
            SNT = s[9:22]

        # find header and mark it
        if s.find("SDIP     SNT") != -1:
            findhead = 1
            if s.find("SDIPP") != -1:
                SDIPP = 6
            else:
                SDIPP = 0

        # find MS-* in
        if s.find("SDIP     SNT") == -1:
            if s.find("MS") != -1:
                MS = s[22 + SDIPP:28 + SDIPP]

        # find main data
        if s.find("VC") != -1:
            MAINDATA = s[42 + SDIPP:].rstrip()
            # print result
            listTpcop.append(SDIP + SNT + MS + MAINDATA)

    if mode == 2:
        # find header and mark it
        if s.find("IEX") != -1:
            listDtstp.append(s)

for x in range(0, len(listTpcop)):
    # print(listTpcop[x] + " -- " +  listDtstp[x])
    outputFile.write(listTpcop[x] + " -- " +  listDtstp[x])
