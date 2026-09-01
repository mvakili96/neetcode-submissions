class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while r >= l:
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                c = (r+l)//2
                if nums[c] < nums[r] and nums[c] < nums[c-1]:
                    return nums[c]
                elif nums[c] < nums[r] and nums[c] > nums[c-1]:
                    r = c - 1
                else:
                    l = c + 1


        