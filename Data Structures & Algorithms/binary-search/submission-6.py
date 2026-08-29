class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r >= l:
            c = (l+r)//2
            if nums[c] > target:
                r = c-1
            elif nums[c] < target:
                l = c+1
            else:
                return c
        return -1

        