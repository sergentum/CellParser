inputFile = open("dip_state.txt", "r")
array = inputFile.readlines()
findhead = 0
SDIPname = ""
for s in array:
    if findhead == 1:
        findhead =0
        SDIPname = s[0:5]
    if s.find("SDIP") == 0:
        print("SDIP found")
        findhead = 1

    print(SDIPname)
    # print(s)

