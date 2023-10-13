#!/usr/bin/env python
import sys

def checkFlag(lookup, row, col, score, steps):
    def isFlag():
        print("checking flag")
        return (lookup[row][col] == "F")
    if(isFlag()):
        score += 5
        steps += 1
        print("FOUND FLAG")
        return True
    return False

def bestPath(matrix, n, pace):
    score = 0 
    steps = 0
    
    lookup = [[0 for i in range(0, n)] for j in range(n)]

    currentCol = 0
    for row in range(0, n):
        if row == n or currentCol == n:
            return score
        
        lookup[row][currentCol] = matrix[row][currentCol]

        if currentCol != n-1: 
            checkFlag(lookup, row, currentCol, score, steps)
            if lookup[row][currentCol+1] == 'O':
               steps += 3
            if lookup[row][currentCol+1] == '.':
                steps += 1
            currentCol += 1
            print("Column", currentCol, "Row", row)
        elif row != n-1:
            checkFlag(lookup, row, currentCol, score, steps)
            if lookup[row+1][currentCol] == 'O':
               steps += 3
            if lookup[row+1][currentCol] == '.':
                steps += 1
            row += 1
            print("Column", currentCol, "Row", row)

def main():
    n = int(input())
    pace = int(input())
    matrix = [[x for x in input().split()] for _ in range(n)]
    
    # print("MATRIX\n", matrix)
    print(bestPath(matrix, n, pace))

if __name__ == "__main__":
  main()