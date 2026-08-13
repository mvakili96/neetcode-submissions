class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for num in nums:
            out_this = []
            for list_ in out:
                out_this.append(list_ + [num])
            out.extend(out_this)
        return out



            
            
            



            
        