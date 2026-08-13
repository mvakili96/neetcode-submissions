class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = ""
        code = ""
        for string in strs:
            lengths = lengths + "(" + str(len(string)) + ")" 
            code = code + string
        
        return lengths + code

    def decode(self, s: str) -> List[str]:
        total_length = 0
        start = 0
        lengths = []
        while total_length != len(s):
            if s[start] == "(":
                start += 1
                num_string = ""
                while s[start] != ")":
                    num_string = num_string + s[start]
                    start += 1

            length_this = int(num_string)
            lengths.append(length_this)
            total_length += length_this + 2 + len(num_string)
            start += 1

        s = s[start:]
        out = []
        for length in lengths:
            out.append(s[:length])
            s = s[length:]

        return out



