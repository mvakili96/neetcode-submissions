class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_length = 0
        for num in nums:
            if num-1 not in set_nums:
                i = 1
                while num+i in set_nums:
                    i += 1

                if i > max_length:
                    max_length = i
        
        return max_length


        