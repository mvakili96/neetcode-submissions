class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]

        for i in range(1,len(nums)):
            prefix.append(nums[i]*prefix[i-1])
            suffix.append(nums[len(nums)-1-i]*suffix[i-1])

        suffix = suffix[::-1]
        out = [suffix[1]]
        for i in range(1,len(nums)-1):
            out.append(prefix[i-1]*suffix[i+1])

        out.append(prefix[len(nums)-2])

        return out    


        