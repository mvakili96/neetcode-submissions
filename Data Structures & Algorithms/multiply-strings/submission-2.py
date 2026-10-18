class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic_ = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        number1 = 0
        for i,item in enumerate(num1[::-1]):
            number1 += dic_[item]*10**i
        number2 = 0
        for i,item in enumerate(num2[::-1]):
            number2 += dic_[item]*10**i       
        
        return str(number1*number2)
                   