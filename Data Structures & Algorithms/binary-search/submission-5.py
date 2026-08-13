class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            cen = (right + left) // 2 
        
            if target > nums[cen]:
                left = cen + 1
            elif target < nums[cen]:
                right = cen - 1
            else:
                return cen
                    
        return -1

        