class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        dic = defaultdict(list)
        for string in strs:
            key = [0]*len(alphabet)
            for char_string in string:
                for i,char in enumerate(alphabet):
                    if char_string == char:
                        key[i] += 1

            dic[tuple(key)].append(string)
        out = []
        for key in dic:
            out.append(dic[key])
        return out 




        