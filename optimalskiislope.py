#!/usr/bin/env python
import sys

def bestPath(matrix, n, pace):    
    lookup = [[0 for _ in range(n)] for _ in range(n)]
    times = [[0 for _ in range(n)] for _ in range(n)]
    numFlags = 0

    for row in range(0, n):
        for col in range(0, n):
            if matrix[row][col] == "O":
                lookup[row][col] = -3
            elif matrix[row][col] == "F":
                lookup[row][col] = -1
                numFlags += 1
            else:
                lookup[row][col] = -1

    def eliminatePath(row, col, score=50) -> int:
        if row == n-1:
            print('Sum of Row',row,'is', sum(lookup[row]))
            score += sum(lookup[row])
            return int(score)
        elif col == n-1:
            print('Sum of Col', col, 'is', sum(lookup[col]))
            score += sum(lookup[col])
            return int(score)
        else:
            scoreOfRow = sum(lookup[row])
            scoreOfCol = sum(lookup[col])

            print('Sum of Row', row,'is', scoreOfRow)
            print('Sum of Rol', col, 'is', scoreOfCol)

            if scoreOfRow > scoreOfCol:
                eliminatePath(row, col+1, score+scoreOfRow)
            elif scoreOfCol > scoreOfRow:
                eliminatePath(row+1, col, score+scoreOfCol)
            else:
                eliminatePath(row, col+1, score+scoreOfRow)
                eliminatePath(row+1, col, score+scoreOfCol)
    
    totalTime = eliminatePath(0, 0)
    score = int(totalTime) - pace
    return score, numFlags 
 
def main():
    n = int(input())
    pace = int(input())
    matrix = [[x for x in input()] for _ in range(n)]
    
    score, numFlags = bestPath(matrix, n, pace)
    print(score, numFlags)

if __name__ == "__main__":
  main()