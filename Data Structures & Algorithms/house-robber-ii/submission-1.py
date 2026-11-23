class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        list_result1 = [nums[0],nums[1],nums[0]+nums[2]]
        for i in range(3,len(nums)-1):
            list_result1.append(nums[i]+max(list_result1[i-2],list_result1[i-3]))
        list_result2 = [nums[1],nums[2],nums[1]+nums[3]]
        for i in range(4,len(nums)):
            list_result2.append(nums[i]+max(list_result2[i-3],list_result2[i-4]))
        
        return max(max(list_result1),max(list_result2))



        