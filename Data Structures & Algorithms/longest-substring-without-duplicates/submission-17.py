class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        max_length = 1
        seen = {s[0]:0}

        for right in range(1,len(s)):
            if s[right] in seen:
                left = max(left,seen[s[right]] + 1)                
            seen[s[right]] = right
            max_length = max(max_length,right-left+1)
        
        return max_length










        