class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_digits(number):
            sum_ = 0
            while number > 0:
                sum_ += (number % 10) * (number % 10)
                number = number // 10
            return sum_

        slow = n
        fast = sum_digits(sum_digits(slow))

        while True:
            if slow == 1:
                return True
            if slow == fast:
                return False
            
            slow = sum_digits(slow)
            fast = sum_digits(sum_digits(fast))

            




        