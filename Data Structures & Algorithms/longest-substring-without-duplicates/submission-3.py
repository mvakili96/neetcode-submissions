class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] not in seen:
                length += 1      
            else:
                if length > max_length:
                    max_length = length
                length = min(i - seen[s[i]],length+1)   
            print(length)
            seen[s[i]] = i
        
        return max(length,max_length)



        