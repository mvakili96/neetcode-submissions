class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append("#")
            res.append(string)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        start = 0
        out = []
        while start<len(s):
            i = start
            while s[start] != "#":
                start += 1
            length_this = int(s[i:start])
            out.append(s[start+1:start+1+length_this])
            start += 1 + length_this

        return out



