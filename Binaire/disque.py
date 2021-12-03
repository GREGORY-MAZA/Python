import os
import shutil


def createRepoIfDoesntExist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def copyFileInRepo(file):
    shutil.copy(file, 'Test Repo')
    print("Le fichier a été copié dans le repo")


def main():
    file = "validtexte.txt"
    directory = "Test Repo"

    createRepoIfDoesntExist(directory)
    copyFileInRepo(file)


if __name__ == '__main__':
    main()