class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        
        lst = [nums[0],nums[1],nums[2]+nums[0]]
        max_this = max(lst)
        for i in range(3,len(nums)):
            lst.append(nums[i]+max(lst[i-2],lst[i-3]))
            max_this = max(max_this,lst[-1])
        return max_this

        