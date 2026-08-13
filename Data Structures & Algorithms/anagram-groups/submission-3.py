class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for string in strs:
            key = [0]*26
            for char_string in string:
                key[ord(char_string)-ord('a')] += 1
            dic[tuple(key)].append(string)
        
        out = []
        for key in dic:
            out.append(dic[key])
        return out 




        