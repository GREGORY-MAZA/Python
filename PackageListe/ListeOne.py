def main():
    L = [13, 15, 12, 17, 15, 18, 15, 17]
    A = 17
    double = 0

    for i in range(len(L)):
        if A == L[i]:
            double = double +1
        if double == 2:
            print("Nous avons trouvé 2 doubles de", A , " dans la liste")
            print(i)
            exit()

    print("Désolé ! pas de double dans la liste")

if __name__ == '__main__':
    main()