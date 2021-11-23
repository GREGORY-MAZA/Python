def main():
    L1 = [5,10,15,20,25]
    L2 = ["Greg","Mati","Steve"]
    L3 = []
    i = 0
    j = 0
    #list_length = len(L1) + len(L2)


    while (i < len(L1) or j < len(L2)):
        if i < len(L1):
            L3.append(L1[i])
            i = i +1
        if j < len(L2):
            L3.append(L2[j])
            j = j +1

    print(L3)


# -----------------------    OTHER VERSION ----------------------


    #while i < list_length:
    #    if i < len(L1):
    #        L3.append(L1[i])
    #    if i < len(L2):
    #        L3.append(L2[i])
    #    i += 1
    #print(L3)

if __name__ == '__main__':
    main()