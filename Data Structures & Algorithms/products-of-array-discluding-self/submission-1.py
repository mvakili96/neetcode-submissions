class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        pre = 1
        suf = 1
        for q in range(len(nums)):
            if q==0:
                prefix.append(1)
            else:
                prefix.append(pre)
            
            pre = pre * nums[q]

            qq = len(nums)-1-q
            if qq==len(nums)-1:
                suffix.append(1)
            else:
                suffix.append(suf)
            
            suf = suf * nums[qq]

        return [x * y for x, y in zip(suffix[::-1], prefix)]

        