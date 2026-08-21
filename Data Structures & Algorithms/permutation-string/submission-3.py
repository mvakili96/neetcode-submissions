class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic_ref = defaultdict(int)
        for char in s1:
            dic_ref[char] += 1

        dic_comp = defaultdict(int)
        for char in s2[:len(s1)]:
            dic_comp[char] += 1

        if dic_ref == dic_comp:
            return True

        for r in range(len(s1),len(s2)):
            dic_comp[s2[r]] += 1
            dic_comp[s2[r-len(s1)]] -= 1

            if dic_comp[s2[r-len(s1)]] <= 0:
                dic_comp.pop(s2[r-len(s1)])

            if dic_ref == dic_comp:
                return True
        
        return False






        