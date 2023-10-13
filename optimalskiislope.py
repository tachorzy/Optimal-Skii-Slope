#!/usr/bin/env python
import sys

def bestPath(matrix, NUMBER_OF_ROWS, NUMBER_OF_COLS, initial_row=0, initial_col=0):
    score, steps = 0

    if initial_row == NUMBER_OF_ROWS and initial_col == NUMBER_OF_COLS:
        return (steps, score//5)
    
    lookup = [[0 for i in range(0, NUMBER_OF_COLS)] for j in range(NUMBER_OF_ROWS)]

    for i in range(0, NUMBER_OF_COLS):
        lookup[i][0] = matrix[i][0]


def main():
  m, n = (int(x) for x in input().split())
  matrix = [[int(x) for x in input().split()] for _ in range(m)]
  print(bestPath(matrix, m, n))

if __name__ == "__main__":
  main()