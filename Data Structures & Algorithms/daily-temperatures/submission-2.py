class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [0]

        for i in range(1,len(temperatures)):

            for q in range(len(stack)-1,-1,-1):
                if temperatures[i] > temperatures[stack[q]]:
                    result[stack[q]] = i - stack[q]
                    stack.pop(q)
                                   
            stack.append(i)
                
        return result






        