class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i,current_list,summ):
            if summ == target:
                result.append(current_list.copy())
                return
            elif i >= len(nums) or summ > target:
                return
            
            current_list.append(nums[i])
            dfs(i,current_list,summ+nums[i])
            current_list.pop()
            dfs(i+1,current_list,summ)
   
        dfs(0,[],0)
        return result
   