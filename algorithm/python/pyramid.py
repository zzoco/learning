def printPyramid(rowsCount):
    for row in range(rowsCount):
        whiteSpace = rowsCount - row - 1
        star = (rowsCount - whiteSpace) * 2 - 1
        
        print((' ' * whiteSpace + '*' * star))

printPyramid(80)
