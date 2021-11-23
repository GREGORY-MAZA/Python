import random


def random_int():
    return random.randint(0, 1000)


def main():
    myListe = []
    while (len(myListe) < 1000):
        myListe.append(random_int())
    myListe.sort()
    print(myListe)


if __name__ == '__main__':
    main()