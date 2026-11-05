class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(i,subsets,subsets_1,counter):
            if i == len(nums):
                return subsets        
            extended = []
            if i >= 1 and nums[i] == nums[i-1]:
                counter += 1
                for lst in subsets_1.copy():
                    lst_this = lst.copy()
                    lst_this.extend(counter*[nums[i]])
                    extended.append(lst_this)
                subsets.extend(extended)
            else:
                subsets_1 = subsets.copy()
                counter = 1
                for lst in subsets.copy():
                    lst_this = lst.copy()
                    lst_this.append(nums[i])
                    extended.append(lst_this)
                subsets.extend(extended)

            return dfs(i+1,subsets,subsets_1,counter)
        result = dfs(0,[[]],[[]],1)

        return result
        