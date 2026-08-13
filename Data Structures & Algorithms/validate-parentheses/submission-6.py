class Solution:
    def isValid(self, s: str) -> bool:
        dic_ = {"(":")","[":"]","{":"}"}
        openn = []
        for char in s:
            if char in dic_:
                openn.append(char)
            else:
                if not openn:
                    return False
                if char == dic_[openn[-1]]:
                    openn.pop()
                else:
                    return False    
        return not openn




        