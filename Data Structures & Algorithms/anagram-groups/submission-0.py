class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        references = defaultdict(list)
        for string in strs:
            dic = defaultdict(int)
            key = [0]*len(alphabet)

            for char in string:
                dic[char] += 1
            for q,char in enumerate(alphabet):
                if char in dic:
                    key[q] = dic[char]
            
            key = tuple(key)
            # print(key)
            references[key].append(string)

        out = []
        for value in references.values():
            out.append(value)
        
        return out
            
            

            

            

                
        