def calculer_Args(*args):
    total = 0
    for num in args:
        total += num
    return total


def calculer_Kwargs(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value
    return total


def concatener_Args(*args):
    concatenationArgs = ""
    for myString in args:
        if myString.startswith('A'):
            concatenationArgs += myString
    return concatenationArgs


def concatener_Kwargs(**kwargs):
    concatenationArgs = ""
    for key, value in kwargs.items():
        if value.startswith('A'):
            concatenationArgs += value
    return concatenationArgs


def main():
    print(calculer_Args(1, 2, 3))
    print(calculer_Kwargs(a=1, b=2, c=4))
    print(concatener_Args("Alpinestar", "Furygan", "Astier", "Kaamelott"))
    print(concatener_Kwargs(a="Alpinestar", b="Furygan", c="Astier", d="Kaamelott"))


if __name__ == '__main__':
    main()