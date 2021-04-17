import math

def rotationX(angle):
  cosine = math.cos(angle)
  sine = math.sin(angle)
  rotation = [
    [1, 0, 0],
    [0, cosine, -sine],
    [0, sine, cosine]
  ]
  return rotation

def rotationY(angle):
  cosine = math.cos(angle)
  sine = math.sin(angle)
  rotation = [
    [cosine, 0, -sine],
    [0, 1, 0],
    [sine, 0, cosine]
  ]
  return rotation

def rotationZ(angle):
  cosine = math.cos(angle)
  sine = math.sin(angle)
  rotation = [
    [cosine, -sine, 0],
    [sine, cosine, 0],
    [0, 0, 1]
  ]
  return rotation


def matrixMultiplication(matrixA, matrixB):
  colsA = len(matrixA[0])
  rowsA = len(matrixA)
  colsB = len(matrixB[0])
  rowsB = len(matrixB)

  result = []
  for i in range(rowsA):
    result.append([0]*colsB)
  if rowsB == colsA:
    for i in range(rowsA):
      for j in range(colsB):
        for k in range(colsA):
          result[i][j] += matrixA[i][k]*matrixB[k][j]
    return result
  raise Exception("Rows of matrix B must match with Columns of matrix A")
  
