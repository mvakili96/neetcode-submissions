class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        max_bits = 1
        res = 0
        for num in range(1,n+1):
            flag = False
            for i in range(max_bits):
                if 1 << i & num-1 != 1 << i:
                    res = res + 1 - i
                    flag = True
                    break  
            if not flag:
                res = 1
                max_bits += 1       
            output.append(res)        
        return output

            
                





              
        
        



        