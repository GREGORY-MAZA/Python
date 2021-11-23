def main():
    Games = ["Forza Horizon 5", "Diablo 2 Ressurected", "World of Warcraft"]        #Déclaration d'un liste
    myGame = "Rocket League"                                                        #Déclaration d'une variable chaine de caracteres
    print(Games)                                                                    #affichage de la liste
    print(Games[0])                                                                 #affichage de l'élément situé en [0] Renvoi Forza Horizon 5
    print(Games[1])                                                                 #affichage de l'élément situé en [0] Renvoi Diablo 2 Ressurected
    print(Games[2])                                                                 #affichage de l'élément situé en [0] renvoi World of Warcraft
    print(myGame[0])                                                                #affichage de l'élément situé en [0] Renvoi R
    Games.append("Mario Bros")                                                      #ajoute dans la liste un nouvel élément
    print(Games)                                                                    #affiche la liste
    Games.remove("World of Warcraft")                                               #retire l'élément "World of Warcraft" de la liste
    print(Games)                                                                    #affiche la liste
    print(len(Games))                                                               #retourne le nombre d'élément dans la liste
    Games.sort()                                                                    #permet de trier par ordre alphabétique les éléments de la liste
    print(Games)                                                                    #affiche la liste



if __name__ == '__main__':
    main()