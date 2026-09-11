class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = nums[0]
        sum_base = nums[0]
        for item in nums[1:]:
            sum_ = max(item, sum_ + item)
            sum_base = max(sum_base, sum_)
        return sum_base
            

        