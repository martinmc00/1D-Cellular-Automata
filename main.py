import pygame

RULE = 90               #Rule applied (decimal)

CEL_SIZE = 10           #Cell size

WIDTH, HEIGHT = 600, 600 #Width and height of the screen displayed
WIN = pygame.display.set_mode((HEIGHT, WIDTH))

pygame.display.set_caption("1-D Cellular Automata")

BG = (0,0,0)            #Background color (Black)
WHITE = (255, 255, 255) #Cells color (White)

ROWS, COLS = int(HEIGHT/CEL_SIZE), int(WIDTH/CEL_SIZE) #Num of rows and cols based on the width and height of the screen

binary_rule = [] #List containing the binary values of the rule applied

first_gen = [0] * COLS #First gen (all zeros)
first_gen[COLS//2] = 1 #All zeros except middle element

generations = [first_gen] #List of all generations

def main():
    global binary_rule

    run = True
    binary_rule = setRule(RULE)
    clock = pygame.time.Clock()

    while run:
        clock.tick(5) #Evolution speed (5 FPS)

        #Checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #Obtaining last generation and calculating the next
        last_generation = generations[-1]
        next_generation = getNextGen(last_generation)

        #Append next generation to the list if there's still room for it
        if(len(generations) < ROWS):
            generations.append(next_generation)

        WIN.fill(BG)

        drawGeneration()        
        
        pygame.display.update()

    pygame.quit()

#Converts the rule in decimal format to binary and splits each number into a list
def setRule(n):
    s = "{0:b}".format(n)
    l = []
    for _ in s:
        l.append(_)

    if(len(l) < 8):         #Checking if the list has 8 elements
        while(len(l) < 8):
            l.insert(0, '0')

    return l


#Draws each generation
def drawGeneration():
    for row, generation in enumerate(generations):
        for x in range(COLS):
            rect = pygame.Rect(x * CEL_SIZE, row * CEL_SIZE, CEL_SIZE, CEL_SIZE)
            if(generation[x] == 1):
                pygame.draw.rect(WIN, WHITE, rect)
            else:
                pygame.draw.rect(WIN, BG, rect)

#Calculates next generation
def getNextGen(current_gen):
    next_gen = [0] * COLS

    for i in range(len(current_gen)):
        leftPosition = ((i-1)+len(current_gen))%len(current_gen)
        leftNeighbor = current_gen[leftPosition]

        current_cel = current_gen[i]

        rightPosition = ((i+1)+len(current_gen))%len(current_gen)
        rightNeighbor = current_gen[rightPosition]

        #Applies rule
        if((leftNeighbor == 1) and (current_cel == 1) and (rightNeighbor == 1)):
            next_gen[i] = int(binary_rule[0])
        elif((leftNeighbor == 1) and (current_cel == 1) and (rightNeighbor == 0)):
            next_gen[i] = int(binary_rule[1])
        elif((leftNeighbor == 1) and (current_cel == 0) and (rightNeighbor == 1)):
            next_gen[i] = int(binary_rule[2])
        elif((leftNeighbor == 1) and (current_cel == 0) and (rightNeighbor == 0)):
            next_gen[i] = int(binary_rule[3])
        elif((leftNeighbor == 0) and (current_cel == 1) and (rightNeighbor == 1)):
            next_gen[i] = int(binary_rule[4])
        elif((leftNeighbor == 0) and (current_cel == 1) and (rightNeighbor == 0)):
            next_gen[i] = int(binary_rule[5])
        elif((leftNeighbor == 0) and (current_cel == 0) and (rightNeighbor == 1)):
            next_gen[i] = int(binary_rule[6])
        elif((leftNeighbor == 0) and (current_cel == 0) and (rightNeighbor == 0)):
            next_gen[i] = int(binary_rule[7])

    return next_gen

if __name__ == "__main__":
    main()