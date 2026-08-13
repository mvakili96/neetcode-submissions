class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        # print(nums)
        out = 0
        out_hist = 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                out += 1
            elif nums[i] == nums[i-1]:
                pass
            else:
                if out > out_hist:
                    out_hist = out
                out = 0

        return max(out_hist,out)+1