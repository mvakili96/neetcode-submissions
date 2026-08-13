class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(num):
            binary = bin(num)
            binary = binary[2:]
            sum_ = 0
            for bit in binary:
                if bit == "1":
                    sum_ += 1
            
            return sum_
        
        out = []
        for num in range(n+1):
            out.append(count_ones(num))
        
        return out


        