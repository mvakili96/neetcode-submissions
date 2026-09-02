class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r >= l:
            if nums[l] <= nums[r]:
                cut = l
                break
            else:
                c = (l+r)//2
                if nums[c] < nums[r] and nums[c] < nums[c-1]:
                    cut = c
                    break
                elif nums[c] < nums[r] and nums[c] > nums[c-1]:
                    r = c - 1
                else:
                    l = c + 1
     
        if nums[cut] <= target and target <= nums[-1]:
            left = cut
            right = len(nums) - 1
        else:
            left = 0
            right = cut     
        while right >= left:
            cen = (right+left)//2
            if nums[cen] == target:
                return cen
            elif nums[cen] < target:
                left = cen + 1
            else:
                right = cen - 1
        return -1


                 
        