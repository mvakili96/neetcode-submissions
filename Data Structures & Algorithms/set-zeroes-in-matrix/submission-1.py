class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        h = len(matrix)
        w = len(matrix[0])
        flag_row_1 = False
        for i in range(h):
            flag = False
            for j in range(w):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    flag = True           
           
            if flag and i != 0:
                matrix[i] = [0] * len(matrix[i])
            
            if flag and i == 0:
                flag_row_1 = True
        
        for j in range(w):
            if matrix[0][j] == 0:
                for i in range(h):
                    matrix[i][j] = 0
        
        if flag_row_1:
            matrix[0] = [0] * len(matrix[0])
        




        
        
        