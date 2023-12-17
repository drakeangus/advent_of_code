#!/bin/python3
import sys    
    
class Cell:
    def __init__(self, letter, row, col):
        self.letter = letter
        self.state = False
        self.row = row
        self.col = col

    def MarkCellTrue(self):
        self.state = True
        try:
            leftCell = matrix[self.row][self.col-1]
            if leftCell.letter.isnumeric() and leftCell.state == False:
                leftCell.MarkCellTrue()
        except IndexError:
            pass

        try:
            rightCell = matrix[self.row][self.col+1]
            if rightCell.letter.isnumeric() and rightCell.state == False:
                rightCell.MarkCellTrue()
        except IndexError:
            pass

        return


def MarkAdjacentCells(row, col, matrix):
    for i in [-1,0,1]:
        for j in [-1, 0, 1]:
    
            try:
                cell = matrix[row+i][col+j]
                if cell.letter.isnumeric():
                     cell.MarkCellTrue()

            except IndexError:
                continue

def ConvertStdinToMatrix(matrix):
    nRow=0
    for line in sys.stdin:
        nCol=0
        line = line.strip()
        row=[]
        for character in line:
            row.append(Cell(character, nRow, nCol))
            nCol+=1
        matrix.append(row)
        nRow+=1

def PrintMatrix(matrix):
    nRow=0
    for row in matrix:
        nCol=0
        for column in row:
            cell = matrix[nRow][nCol]
            if cell.state:
                print('\033[38;5;10m'+cell.letter+'\033[0;0m', end="")
            else:
                print(cell.letter, end="")
            nCol+=1
        nRow+=1
        print()

def MarkCellsNextToSymbols(matrix):
# loop through matrix and mark adjacent cells
    nRow=0
    for row in matrix:
        nCol=0
        for column in row:
            character = matrix[nRow][nCol].letter
            if not character.isnumeric() and character != ".":
                MarkAdjacentCells(nRow, nCol, matrix)
            nCol+=1
        nRow+=1

def SumMarkedNumbers(matrix):
    nRow=0
    sum=0
    for row in matrix:
        num_str=""
        nCol=0
        for column in row:
            cell = matrix[nRow][nCol]
            if cell.state:
                num_str += cell.letter
            elif not num_str == "":
                sum += int(num_str)
                num_str=""
            nCol+=1

        if not num_str == "":
            sum += int(num_str)
            num_str=""
        nRow+=1
print(sum)

matrix = []
ConvertStdinToMatrix(matrix)
MarkCellsNextToSymbols(matrix)
PrintMatrix(matrix)
SumMarkedNumbers(matrix)


print("Done!")
