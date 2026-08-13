class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)
        n = n[2:]
        n = (32-len(n))*"0" + n
        return int(n[::-1],2)        