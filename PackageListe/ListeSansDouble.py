def main():
    L1 = [13, 15, 12, 17, 15]
    L2 = [18, 15, 14, 13, 19, 20]
    L3 = []


    for i in range(len(L1)):
        if L1[i] not in L3:
            L3.append(L1[i])
            print(L3)
    for j in range(len(L2)):
        if L2[j] not in L3:
            L3.append(L2[j])
            print(L3)

if __name__ == '__main__':
    main()
