class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_ = max(nums)
        min_ = min(nums)

        if max_ - min_ == len(nums) - 1 and min_ != 0:
            return 0
        elif max_ - min_ == len(nums) - 1 and min_ == 0:
            return max_ + 1

        out = 0
        range_ = [i for i in range(min_,max_+1)]
        nums.append(0)
        for i in range(len(nums)):
            out ^= nums[i] ^ range_[i]

        return out