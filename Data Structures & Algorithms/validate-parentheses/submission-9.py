class Solution:
    def isValid(self, s: str) -> bool:
        dic_ = {"(":")","[":"]","{":"}"}
        opens = []
        for item in s:
            if item in dic_:
                opens.append(item)
            else:
                if not opens:
                    return False
                if item == dic_[opens[-1]]:
                    opens.pop()
                else:
                    return False        
        return not opens







        