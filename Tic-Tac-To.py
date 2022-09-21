#**************************************************************************************************
#**** Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row,    ****
#**** a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid ****
#**** of nine squares.                                                                         **** 
#**** 21.09.2022.                                                                              **** 
#**** Rubén Zempoalteca.                                                                       **** 
#**************************************************************************************************
def main():
    jugador = jugadores("")
    #print (jugador)
    tarima = crea_tarima()
    while not (tarima_llena(tarima) == True or un_ganador(tarima) == True):
        dibuja_tarima(tarima)
        jugada(jugador, tarima)
        jugador = jugadores(jugador)
    dibuja_tarima(tarima)
    print("Game over. Thanks for playing!")
    
def crea_tarima():
    tarima = []
    for cuadro in range(9):
        tarima.append(cuadro + 1)
    return tarima

def dibuja_tarima(tarima):
    print()
    print(f"{tarima[0]}|{tarima[1]}|{tarima[2]}")
    print('-+-+-')
    print(f"{tarima[3]}|{tarima[4]}|{tarima[5]}")
    print('-+-+-')
    print(f"{tarima[6]}|{tarima[7]}|{tarima[8]}")
    print()

def jugadores(actual):
    if actual == "" or actual == "0":
        return "x"
    elif actual == "x":
        return "0"   

def jugada(jugador, tarima):
    grid = int(input(f"Player {jugador} your turn, select a number between 1 and 9: "))
    tarima[grid - 1] = jugador     

def tarima_llena(tarima):
    for grid in range(9):
        if tarima[grid] !="x" and tarima[grid] != "0":
            return False
    return True   

def un_ganador (tarima):
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
