#!/usr/bin/env python
import sys

def bestPath(matrix, NUMBER_OF_ROWS, NUMBER_OF_COLS, pace):
    score = 0 
    steps = 0
    
    lookup = [[0 for i in range(0, NUMBER_OF_COLS)] for j in range(NUMBER_OF_ROWS)]

    currentCol = 0
    for row in range(0, NUMBER_OF_COLS):
        lookup[row][0] = matrix[row][0]

        if row == NUMBER_OF_ROWS and currentCol == NUMBER_OF_COLS:
            return score
        if lookup[row][currentCol] == 'F':
           score += 5
           steps += 1
           row += 1
        elif currentCol != NUMBER_OF_COLS-1: 
            if lookup[row][currentCol+1] == 'O':
               steps += 3
            if lookup[row][currentCol+1] == '.':
                steps += 1
            currentCol += 1
        elif row != NUMBER_OF_ROWS-1:
            if lookup[row+1][currentCol] == 'O':
               steps += 3
            if lookup[row+1][currentCol] == '.':
                steps += 1
            row += 1
            
def main():
    n = int(input())
    pace = int(input())
    matrix = [[x for x in input().split()] for _ in range(n)]
    print(bestPath(matrix, n, n, pace))

if __name__ == "__main__":
  main()