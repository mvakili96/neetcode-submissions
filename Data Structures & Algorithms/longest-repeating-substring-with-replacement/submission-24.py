class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        seen = [0]*26
        seen[ord(s[left])-ord('A')] += 1
        max_freq = 1
        for right in range(1,len(s)):
            seen[ord(s[right])-ord('A')] += 1
            max_freq = max(max_freq,seen[ord(s[right])-ord('A')])
            if right - left + 1 > max_freq + k:
                seen[ord(s[left])-ord('A')] -= 1
                left += 1
        return right - left + 1





 









        









        