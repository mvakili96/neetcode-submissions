class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        max_repeat = 0
        left = 0
        answer = 0
        for right in range(len(s)):
            seen[s[right]] += 1
            max_repeat = max(max_repeat,seen[s[right]])

            window_length = right - left + 1
            while window_length - max_repeat > k:
                seen[s[left]] -= 1
                window_length -= 1
                left += 1


            answer = max(window_length,answer)

        return answer








        









        