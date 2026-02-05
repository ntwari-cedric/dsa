from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        
        # FIX 1: make prefix an instance variable
        self.prefix = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    self.prefix[i][j] = matrix[i][j]
                elif i == 0:
                    self.prefix[i][j] = self.prefix[i][j-1] + matrix[i][j]
                elif j == 0:
                    self.prefix[i][j] = self.prefix[i-1][j] + matrix[i][j]
                else:
                    self.prefix[i][j] = (
                        self.prefix[i-1][j]
                        + self.prefix[i][j-1]
                        - self.prefix[i-1][j-1]
                        + matrix[i][j]
                    )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = self.prefix[row2][col2]
        
        if col1 > 0:
            answer -= self.prefix[row2][col1-1]
        if row1 > 0:
            answer -= self.prefix[row1-1][col2]
        if row1 > 0 and col1 > 0:
            answer += self.prefix[row1-1][col1-1]
        
        return answer
