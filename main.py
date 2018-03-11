inputFile = open("dip_state.txt", "r")
array = inputFile.readlines()
findhead = 0
SDIP = ""
SNT = ""
MS = ""
MAINDATA = ""
SDIPP = 6
for s in array:

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
        print(SDIP + SNT + MS + MAINDATA)
