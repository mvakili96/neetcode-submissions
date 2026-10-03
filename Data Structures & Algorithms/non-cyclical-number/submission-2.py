class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        num_this = n
        while True:
            sum_ = 0
            while num_this > 0:
                digit = num_this % 10
                sum_ += digit * digit
                num_this = num_this // 10
            if sum_ == 1:
                return True
            else:
                if sum_ in seen:
                    return False
                seen.add(sum_)
                num_this = sum_
            




        