class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        res = 0
        for i in range(2,len(n)):
            if n[i] == "1":
                res += 1

        return res