class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        dic_ = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

        multiplications = []
        for enum,i in enumerate(num1[::-1]):
            mul_i = "0" * enum
            residual = 0
            for j in num2[::-1]:
                mul_i = str((dic_[i]*dic_[j]+residual)%10) + mul_i
                residual = (dic_[i]*dic_[j]+residual) // 10

            if residual > 0:
                mul_i = str(residual) + mul_i
            multiplications.append(mul_i)

        max_len = 0
        for string in multiplications:
            max_len = max(len(string),max_len)
        
        for i in range(len(multiplications)):
            if len(multiplications[i])<max_len:
                multiplications[i] = "0" * (max_len-len(multiplications[i])) + multiplications[i]
        
        residual = 0
        output = ""
        for i in range(max_len-1,-1,-1):    
            addition_i = residual
            for j in range(len(multiplications)):
                addition_i += dic_[multiplications[j][i]]
            
            residual = addition_i // 10
            output = str(addition_i%10) + output
        
        if residual > 0:
            output = str(residual) + output

        return output
                   