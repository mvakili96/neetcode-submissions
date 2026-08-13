class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_ = max(nums)
        hash_ = set(nums)
        for i in range(0,max_+1):
            if i not in hash_:
                return i
        return i+1