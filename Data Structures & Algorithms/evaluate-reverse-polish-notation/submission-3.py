class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums    = []
        for item in tokens:
            if item.lstrip('-').isdigit():
                nums.append(item)
            else:
                if item == "/":
                    a = int(nums[-2])
                    b = int(nums[-1])
                    result = int(a / b) 
                else:
                    result = eval(nums[-2] + item + nums[-1])

                nums.pop()
                nums.pop()
                nums.append(str(result))
        
        return(int(float(nums[0])))




        