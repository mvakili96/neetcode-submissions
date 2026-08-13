class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        lengths = []
        for string in strs:
            code += string
            lengths.append(len(string))
        
        lengths = str(lengths)
        code += lengths
        return code

    def decode(self, s: str) -> List[str]:
        list_out = []
        lengths = []
        flag_digit = False
        num = ""
        for i in range(len(s)-2,-1,-1):
            if s[i] == " " or s[i] == "," or s[i] == "[":
                flag_digit = False
            else:
                flag_digit = True
                num = s[i] + num
            
            if not flag_digit and len(num)>0:
                lengths.append(int(num))
                num = ""

            if s[i] == "[":
                break

        lengths = lengths[::-1]

        for length in lengths:
            string_this = s[:length]
            list_out.append(string_this)
            s = s[length:]


        return list_out
