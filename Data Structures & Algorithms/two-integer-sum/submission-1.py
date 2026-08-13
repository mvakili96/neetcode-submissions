class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i,item in enumerate(nums):
            diff = target-item

            if diff in hash_map:
                return [hash_map[diff],i]
            
            hash_map[item] = i

            

        