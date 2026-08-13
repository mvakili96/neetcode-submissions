class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for num in nums:
            out_this = []
            len_out = len(out)
            for i in range(len_out):
                out.append(out[i] + [num])
        return out



            
            
            



            
        