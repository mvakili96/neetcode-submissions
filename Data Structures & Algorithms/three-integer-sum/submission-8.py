class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def find_two(numbers,target):
            left = 0
            right = len(numbers) - 1
            out = []
            while left < right:
                if numbers[right] + numbers[left] == target:
                    out.append([numbers[left],numbers[right],-target])
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1                    
                elif numbers[right] + numbers[left] < target:
                    left += 1
                else:
                    right -= 1    
            return out

        nums.sort()
        out = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            triplets = find_two(nums[i+1:],-nums[i])
            if triplets:
                out.extend(triplets)  
        return out



        
        