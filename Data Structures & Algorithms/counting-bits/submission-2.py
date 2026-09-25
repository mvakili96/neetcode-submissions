class Solution:
    def countBits(self, n: int) -> List[int]:
        max_bits = 32
        res = 0
        for i in range(32):
            if (1 << i) & n == (1 << i):
                res += 1
                max_bits = i
        
        output = [res]
        for num in range(n-1,-1,-1):
            res = 0
            for i in range(max_bits+1):
                if (1 << i) & num == (1 << i):
                    res += 1

            output.append(res)
        
        return output[::-1]



              
        
        



        