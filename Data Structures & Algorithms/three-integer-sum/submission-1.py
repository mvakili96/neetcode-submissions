class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            numbers = nums[:]
            target = -nums[i]         
            numbers.remove(nums[i])
            left = 0
            right = len(numbers) - 1
            while left < right:
                if numbers[left] + numbers[right] > target:
                    right -= 1
                elif numbers[left] + numbers[right] < target:
                    left += 1
                else:
                    output.append(sorted([nums[i],numbers[left],numbers[right]]))
                    right -= 1
                    left += 1
        
        return list(set(tuple(x) for x in output))

        
        