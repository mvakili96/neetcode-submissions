class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[right] < nums[left]:
            while right - left > 1:
                cen = (left + right) // 2

                if nums[cen] > nums[right]:
                    left = cen
                else:
                    right = cen
            
            cut = right
            if target <= nums[-1]:
                left = cut
                right = len(nums)-1
            else:
                left = 0
                right = cut
                
        # print(left,right)
        while left <= right:
            cen = (left + right) // 2

            if nums[cen] < target:
                left = cen + 1
            elif nums[cen] > target:
                right = cen - 1
            else:
                return cen
            
        return -1
                 
        