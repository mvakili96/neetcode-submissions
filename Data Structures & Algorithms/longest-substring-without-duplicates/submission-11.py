class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 1
        length = 1
        max_length = 1
        seen = {}
        seen[s[0]] = 0
        while right < len(s):
            if s[right] not in seen:
                length += 1
                seen[s[right]] = right
            else:
                left = max(left,seen[s[right]] + 1)
                seen[s[left]] = left
                seen[s[right]] = right
                length = right - left + 1
            right += 1
            max_length = max(max_length,length)
        return max_length






        