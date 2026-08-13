class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num] += 1
        
        numbers = [[] for _ in range(len(nums))]
        for key in dict_:
            numbers[dict_[key]-1].append(key)
                
        out = []
        while True:
            for list_ in numbers[::-1]:
                for element in list_:
                    out.append(element)
                    if len(out) == k:
                        return out



        