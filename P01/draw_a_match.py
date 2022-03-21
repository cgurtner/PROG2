from random import randint

def drawBoard(matches):
    match = '========O'

    for r in range(matches):
        print(match)

    print('| the stack has ' + str(matches) + ' matches. |', end='\n')
    print()

def drawAI(matches):
    if matches % 4 == 1:
        draw = randint(1, 3)
        matches = matches - draw
        print('AI draws ' + str(draw) + ' matches. \n')
    else:
        draw = (matches - 1) % 4
        matches = matches - draw
        print('AI draws '  + str(draw) + ' matches. \n')

    return matches

def drawPlayer(matches):
    print('How many matches do you wanna draw?')
    print('There are ' + str(matches) + ' matches left.')
    
    max = matches if matches <= 3 else 3
    min = 1

    drawStr = 'draw '
    for r in range(min, max+1):
        drawStr += str(r) + ','
    drawStr = drawStr[:-1] + ' matches: \n'
    draw = int(input(drawStr))

    print('\nPlayer draws ' + str(draw) + ' matches. \n')

    if draw == 1 or draw == 2 or draw == 3:
        matches = matches - draw
    else:
        matches = drawPlayer(matches)
    
    return matches

matches = randint(10, 20)
player = randint(1,6) % 2 == 0 # if True (0) then the real player is playing next, else the AI
print('Game is starting with ' + str(matches) + ' matches.\n')

while matches > 0:
    if player:
        matches = drawPlayer(matches)
        player = not player
    else:
        matches = drawAI(matches)
        player = not player

    drawBoard(matches)

endStr = 'Player ' if player else 'AI '
endStr += 'has won the match!'
print(endStr)
