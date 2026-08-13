class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if not matrix[0]:
        #     return -1
        
        chosen_row = None
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                chosen_row = row
                break
        
        if chosen_row:
            left = 0
            right = len(chosen_row) - 1

            while left <= right:
                cen = (left+right)//2
                if chosen_row[cen] < target:
                    left = cen + 1
                elif chosen_row[cen] > target:
                    right = cen - 1
                else:
                    return True
        else:
            return False

        return False




        