def calculateArgs(*args):
    total = 0
    for num in args:
        total += num
    return total


def calculateKwargs(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value
    return total


def concateArgs(*args):
    concatenationArgs = ""
    for myString in args:
        if myString.startswith('A'):
            concatenationArgs += myString
    return concatenationArgs


def concateKwargs(**kwargs):
    concatenationArgs = ""
    for key, value in kwargs.items():
        if value.startswith('A'):
            concatenationArgs += value
    return concatenationArgs


def main():
    print(calculateArgs(1, 2, 3))
    print(calculateKwargs(a=1, b=2, c=4))
    print(concateArgs("Albert", "Hervé", "Alfred", "Michel"))
    print(concateKwargs(a="Albert", b="Hervé", c="Alfred", d="Michel"))


if __name__ == '__main__':
    main()