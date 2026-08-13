class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_1 = defaultdict(int)
        dict_2 = defaultdict(int)

        for char in s1:
            dict_1[char] += 1
        
        for r in range(len(s2)):
            dict_2[s2[r]] += 1
            if r < len(s1) - 1:
                continue
            elif r > len(s1) - 1:
                dict_2[s2[r-len(s1)]] -= 1
                if dict_2[s2[r-len(s1)]] == 0:
                    dict_2.pop(s2[r-len(s1)], None)
            
            if dict_1 == dict_2:
                return True
            
        return False


        