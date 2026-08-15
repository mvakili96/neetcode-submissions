class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def find_two(numbers,target):
            left = 0
            right = len(numbers) - 1
            out = []
            while left < right:
                if numbers[right] + numbers[left] == target:
                    out.append([numbers[left],numbers[right],-target])
                    right -= 1
                    left += 1                      
                elif numbers[right] + numbers[left] < target:
                    left += 1
                else:
                    right -= 1    
            return out

        nums.sort()
        out = []
        for i in range(len(nums)):
            numbers = nums[i+1:]
            triplets = find_two(numbers,-nums[i])
            for triplet in triplets:
                if triplet not in out:
                    out.append(triplet)  
        return out



        
        