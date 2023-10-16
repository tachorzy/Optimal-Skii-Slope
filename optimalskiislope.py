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

# def bestPath(matrix, n, pace):
#     score = 0 
#     steps = 0
    
#     lookup = [[0 for _ in range(n)] for _ in range(n)]

#     currentCol = 0
#     print('n received as', n)
#     for row in range(0, n+1):
#         if row == n or currentCol == n:
#             return pace-steps, score//5
#         print("Column equals:", currentCol, "Row equals:", row)
#         lookup[row][currentCol] = matrix[row][currentCol]

#         print("Score is currently:", score)
#         print("Steps is currently:", steps)
#         if currentCol != n-1: 
#             if checkFlag(lookup, row, currentCol): 
#                 score += 5
#                 steps += 1
#             elif lookup[row][currentCol+1] == 'O':
#                print("OBSTACLE!")
#                steps += 3
#             elif lookup[row][currentCol+1] == '.':
#                 steps += 1
#             currentCol += 1
#             print("Column", currentCol, "Row", row)
#         elif row != n-1:
#             if checkFlag(lookup, row, currentCol):
#                 score += 5
#                 steps += 1
#             elif lookup[row+1][currentCol] == 'O':
#                steps += 3
#             elif lookup[row+1][currentCol] == '.':
#                 steps += 1
#             row += 1
#             print("Column", currentCol, "Row", row)

def bestPath(matrix, n, pace):    
    lookup = [[[0, 0] for _ in range(n)] for _ in range(n)]
    times = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(1, n):
        # south
        obstacleAddedTime = 3 if matrix[i][0] == 'O' else 1
        flagPoints = 5 if matrix[i][0] == 'F' else 0

        currentNodeInFirstColumn = lookup[i][0]
        northernNodeInFirstColumn = lookup[i-1][0]

        if flagPoints == 5:
            print("FOUND FLAG IN FIRST COLUMN AT ", i, 0)
            currentNodeInFirstColumn[1] = northernNodeInFirstColumn[1] + 1 

        times[i][0] = northernNodeInFirstColumn[0] + obstacleAddedTime
        currentNodeInFirstColumn[0] = northernNodeInFirstColumn[0] + flagPoints

        obstacleAddedTime = 3 if matrix[0][i] == 'O' else 1
        flagPoints = 5 if matrix[0][i] == 'F' else 0

        currentNodeInFirstRow = lookup[0][i]
        westernNodeInFirstRow = lookup[0][i-1]


        if flagPoints == 5:
            currentNodeInFirstRow[1] = westernNodeInFirstRow[1] + 1 


        times[0][i] = times[0][i - 1] + obstacleAddedTime
        currentNodeInFirstRow[0] = westernNodeInFirstRow[0] + flagPoints

    for i in range(1, n):
        for j in range(1, n):
            obstacleAddedTime = 3 if matrix[i][j] == 'O' else 1
            flagPoints = 5 if matrix[i][j] == 'F' else 0

            timeFromTop = times[i-1][j]
            timeFromLeft = times[i][j-1]
            
            currentWesternNode = lookup[i-1][j]
            currentNorthernNode = lookup[i][j-1]

            currentNode = lookup[i][j]

            if currentWesternNode[0] + flagPoints - (timeFromTop - pace) > currentNorthernNode[0] + flagPoints - (timeFromLeft - pace):
                currentNode[0] = currentWesternNode[0] + flagPoints
                times[i][j] = timeFromTop + obstacleAddedTime
                currentNode[1] = currentWesternNode[1] 
            else:
                currentWesternNode[0] = currentNorthernNode[0] + flagPoints 
                times[i][j] = timeFromLeft + obstacleAddedTime
                currentNode[1] = currentNorthernNode[1]          
            
            if matrix[i][j] == 'F':
                lookup[i][j][1] += 1 

    totalTime = times[n-1][n-1]
    differenceInTime = totalTime - pace
    flags = lookup[n-1][n-1][1]
    score = 5 * flags - differenceInTime

    return score, flags 
 
def main():
    n = int(input())
    pace = int(input())
    matrix = [[x for x in input()] for _ in range(n)]
    
    score, numFlags = bestPath(matrix, n, pace)
    print(score, numFlags)

if __name__ == "__main__":
  main()