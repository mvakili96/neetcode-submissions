class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while left < right:
            area_this = min(heights[left],heights[right]) * (right-left)
            if area_this > area:
                area = area_this

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1        
        return area