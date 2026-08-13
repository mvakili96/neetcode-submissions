class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = defaultdict(int)
        out = []
        for item in nums:
            dict_[item] += 1
        
        occurances = dict_.values()
        occurances = sorted(occurances)
        occurances = occurances[::-1]
        occurances = occurances[:k]
        for key in dict_:
            if dict_[key] in occurances:
                out.append(key)
        
        return out


            

        
        