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
        
        set_operations = set()
        for item in '+-*/':
            set_operations.add(item)

        nums = []
        for char in tokens:
            if char in set_operations:
                a = nums.pop()
                b = nums.pop()
                nums.append(operation(char,b,a))
            else:
                nums.append(int(char))

        return nums[0]





        