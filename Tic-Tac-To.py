#**************************************************************************************************
#**** Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row,    ****
#**** a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid ****
#**** of nine squares.                                                                         **** 
#**** 21.09.2022.                                                                              **** 
#**** Rubén Zempoalteca.                                                                       **** 
#**************************************************************************************************
def main():
    jugador = jugadores("") #Begin the game with X player
    #print (jugador)
    tarima = crea_tarima() #set up an array to create a grid of the game
    while not (tarima_llena(tarima) == True or un_ganador(tarima) == True): # do until no winner or full grid
        dibuja_tarima(tarima) #Draw grid of the game with the movement of the player on turn
        jugada(jugador, tarima) #Ask to the player choose a number between 1 and 9 (movement of the player)
        jugador = jugadores(jugador) #Turn of the 0 player or X player
    dibuja_tarima(tarima) #Draw the grid of the game with all the players movement
    print("Game over. Thanks for playing!") #End of game
    
def crea_tarima():
    #set up an array of 9 elements to create a grid of the game
    tarima = []
    for cuadro in range(9):
        tarima.append(cuadro + 1)
    return tarima

def dibuja_tarima(tarima):
    #Fill the matrix with the numbers from 1 to 9 to draw the game grid
    print()
    print(f"{tarima[0]}|{tarima[1]}|{tarima[2]}")
    print('-+-+-')
    print(f"{tarima[3]}|{tarima[4]}|{tarima[5]}")
    print('-+-+-')
    print(f"{tarima[6]}|{tarima[7]}|{tarima[8]}")
    print()

def jugadores(actual):
    #There are two players for the game (X and 0)
    #To identify a player and begin the game with X player
    if actual == "" or actual == "0": #Identify if is the turn of X player
        return "x"
    elif actual == "x": #Set the turn of the 0 player
        return "0"   

def jugada(jugador, tarima):
    #Ask to the player choose a number between 1 and 9 to replace the number position with X or 0 depending on the player in turn
    turno = int(input(f"Player {jugador} your turn, select a number between 1 and 9: "))
    tarima[turno - 1] = jugador # replace number position with X or 0    

def tarima_llena(tarima):
    #Determine if the grid is full and there is no winner
    for grilla in range(9):
        if tarima[grilla] !="x" and tarima[grilla] != "0":
            return False
    return True   

def un_ganador (tarima):
    #determine if there is a winner identifying if there is a row, column or diagonal of X or 0
    ganador = (tarima[0] == tarima[4] == tarima[8] or  #diagonals 
                tarima[2] == tarima[4] == tarima[6] or  #diagonals
                tarima[0] == tarima[3] == tarima[6] or  #columns
                tarima[1] == tarima[4] == tarima[7] or  #columns
                tarima[2] == tarima[5] == tarima[8] or  #columns
                tarima[0] == tarima[1] == tarima[2] or  #rows
                tarima[3] == tarima[4] == tarima[5] or  #rows
                tarima[6] == tarima[7] == tarima[8] )   #rows
    return ganador            
                                                        

main()
