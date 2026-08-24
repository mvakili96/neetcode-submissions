class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(char,a,b):
            if char == '+':
                return a+b
            elif char == '-':
                return a-b
            elif char == '*':
                return a*b
            elif char == '/':
                return int(a/b)
        
        nums = []
        for char in tokens:
            if char in '+-*/':
                a = nums.pop()
                b = nums.pop()
                nums.append(operation(char,b,a))
            else:
                nums.append(int(char))

        return nums[0]





        