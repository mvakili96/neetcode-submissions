class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen = defaultdict(int)
        seen[s[left]] += 1
        max_freq = 1
        max_length = 1
        for right in range(1,len(s)):
            seen[s[right]] += 1
            max_freq = max(max_freq,seen[s[right]])
            if right - left + 1 > max_freq + k:
                seen[s[left]] -= 1
                left += 1
            max_length = right - left + 1
        return max_length





 









        









        