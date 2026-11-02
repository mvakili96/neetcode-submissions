class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(j,current_result):
            if j == len(nums):
                return current_result

            results = []
            for lst in current_result:
                for i in range(len(lst)+1):
                    lst_this = lst.copy()
                    lst_this.insert(i,nums[j])
                    results.append(lst_this)
            
            return dfs(j+1,results)

        return dfs(1,[[nums[0]]])






        return result

                
        