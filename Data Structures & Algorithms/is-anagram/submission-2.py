class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for char in s:
            dict_s[char] += 1
        for char in t:
            dict_t[char] += 1

        if dict_s == dict_t:
            return True
        else:
            return False 


        