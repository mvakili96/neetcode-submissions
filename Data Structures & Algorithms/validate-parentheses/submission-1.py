class Solution:
    def isValid(self, s: str) -> bool:
        open_  = {'(':0,'[':1,'{':2}
        close_ = [')',']','}']

        close_index_list = []
        for char in s:
            if char in open_:
                close_index_list.append(open_[char])
            elif char in close_ and close_index_list:
                close_index = close_index_list[-1]
                if char == close_[close_index]:
                    close_index_list.pop()
                else:
                    return False
            else:
                return False
        
        if close_index_list:
            return False
        else:
            return True



        