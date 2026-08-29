class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                l = 0
                r = len(matrix[0]) - 1
                while r >= l:
                    cen = (r+l) // 2

                    if matrix[i][cen] == target:
                        return True
                    elif matrix[i][cen] < target:
                        l = cen + 1
                    else:
                        r = cen - 1     
        return False

                






        