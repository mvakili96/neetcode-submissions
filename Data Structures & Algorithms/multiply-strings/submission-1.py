class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic_ = {}
        for i in range(10):
            dic_[str(i)] = i
        
        number1 = 0
        for i,item in enumerate(num1[::-1]):
            number1 += dic_[item]*10**i
        number2 = 0
        for i,item in enumerate(num2[::-1]):
            number2 += dic_[item]*10**i       
        
        return str(number1*number2)
                   