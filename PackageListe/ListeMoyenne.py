def calculer_moyenne(notes, coeff):
    stock_calculate = []
    for i in range(len(notes)):
        element = notes[i] * coeff[i]
        stock_calculate.append(element)
    print(sum(stock_calculate)/sum(coeff))


def main():
    Val = [12.5, 13.6, 18.4, 9.7]
    Coeff = [2, 3, 5, 4]
    return calculer_moyenne(Val, Coeff)


if __name__ == '__main__':
    main()
