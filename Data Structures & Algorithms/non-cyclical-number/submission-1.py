class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_square_digits(num):
            string = str(num)
            sum_ = 0
            for char in string:
                sum_ += int(char)*int(char)
            
            return sum_

        hash_set = set()
        result = sum_square_digits(n)

        while result not in hash_set:
            if result == 1:
                return True
            else:
                hash_set.add(result)
                result = sum_square_digits(result)

        return False        