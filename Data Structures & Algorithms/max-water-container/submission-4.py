class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_volume = 0
        while right - left >= 1:
            if (right-left)*min(heights[left],heights[right]) > max_volume:
                max_volume = (right-left)*min(heights[left],heights[right])
            
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_volume