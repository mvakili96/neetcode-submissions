class Solution:
    def getSum(self, a: int, b: int) -> int:
        residual = 0
        out = 0
        for i in range(32):
            a_bit = (1<<i) & a
            b_bit = (1<<i) & b

            interim_result = a_bit ^ b_bit ^ residual<<i
            out = out | interim_result
            if residual == 0 and a_bit & b_bit != 0:
                residual = 1
            elif residual == 1 and (a_bit | b_bit != 0):
                residual = 1
            else:
                residual = 0

        return out if out < (1 << 31) else ~(out ^ 0xFFFFFFFF)


            





        