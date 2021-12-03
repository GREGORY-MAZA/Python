import numpy as np


def readBinaryFile():
    with open('data.bin', 'rb') as f:
        rectype = np.dtype(np.int32)
        bdata = np.fromfile(f, dtype=rectype)

    return bdata


def writeBinaryFile():
    with open('data.bin', 'wb') as binFile:
        num = [1, 4, 8, 5, 78, 1, 4, 8, 5, 78, 1, 4, 8, 5, 90]
        myList = bytearray(num)
        binFile.write(myList)


def main():
    writeBinaryFile()
    print(readBinaryFile())


if __name__ == '__main__':
    main()