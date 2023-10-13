#!/usr/bin/env python
import sys

def checkFlag(lookup, row, col):
    def isFlag():
        print("checking flag")
        if lookup[row][col] == 'O':
            return True
        return False    
    if(isFlag()):
        print("FOUND FLAG")
        return True
    return False

def bestPath(matrix, n, pace):
    score = 0 
    steps = 0
    
    lookup = [[0 for _ in range(n)] for _ in range(n)]

    currentCol = 0
    print('n received as', n)
    for row in range(0, n+1):
        if row == n or currentCol == n:
            return steps, score//5
        print("Column equals:", currentCol, "Row equals:", row)
        lookup[row][currentCol] = matrix[row][currentCol]

        print("Score is currently:", score)
        print("Steps is currently:", steps)
        if currentCol != n-1: 
            if checkFlag(lookup, row, currentCol): 
                score += 5
                steps += 1
            elif lookup[row][currentCol+1] == 'O':
               print("OBSTACLE!")
               steps += 3
            else:
                steps += 1
            currentCol += 1
            print("Column", currentCol, "Row", row)
        elif row != n-1:
            if checkFlag(lookup, row, currentCol):
                score += 5
                steps += 1
            elif lookup[row+1][currentCol] == 'O':
               steps += 3
            else:
                steps += 1
            row += 1
            print("Column", currentCol, "Row", row)

def main():
    n = int(input())
    pace = int(input())
    matrix = [[x for x in input()] for _ in range(n)]
    
    print('N', n, 'Pace', pace)
    print('size of matrix', len(matrix))
    
    for i in range(0, n):
        for j in range(0, n):
            print(matrix[i][j], end="")
        print()
    # print("MATRIX\n", matrix)
    print(bestPath(matrix, n, pace))

if __name__ == "__main__":
  main()