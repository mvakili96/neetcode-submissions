class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] >= nums[0]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while right - left > 1:
            cen = (left + right) // 2

            if nums[cen] < nums[right]:
                right = cen
            elif nums[cen] > nums[right]:
                left = cen
            else:
                return nums[left]
        
        return nums[right]


        