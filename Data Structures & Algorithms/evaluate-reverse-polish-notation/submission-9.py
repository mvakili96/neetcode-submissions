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
            if char.isdigit() or (char.startswith('-') and char[1:].isdigit()):
                nums.append(int(char))
            else:
                a = nums.pop()
                b = nums.pop()
                nums.append(operation(char,b,a))

        return nums[0]





        