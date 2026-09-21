class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            num = 1 << i
            if num & n == num:
                res += 1
        
        return res
