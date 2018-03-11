inputFile = open("dip_state.txt", "r")
array = inputFile.readlines()
findhead = 0
SDIP = ""
SNT = ""
MS = ""
for s in array:
    # work with string after header
    if findhead == 1:
        findhead = 0
        SDIP = s[0:8]
        SNT = s[9:22]

    # find header and mark it
    if s.find("SDIP     SNT") != -1:
        findhead = 1

    # find MS-* in
    if s.find("SDIP     SNT") == -1:
        if s.find("MS") != -1:
            MS = s[22:28]

    # print(s.find("MS-"))

    print(SDIP + SNT + MS)
    # print(s)

