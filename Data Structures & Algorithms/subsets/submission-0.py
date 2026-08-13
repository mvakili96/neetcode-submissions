class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for num in nums:
            out_this = []
            for list_ in out:
                list_this = list_ + [num]
                out_this.append(list_this)
            out.extend(out_this)
        
        return out



            
            
            



            
        