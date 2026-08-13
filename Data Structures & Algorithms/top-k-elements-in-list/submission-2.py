class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num] += 1
        
        numbers = []
        freq = []
        for key in dict_:
            numbers.append(int(key))
            freq.append(dict_[key])
        
        freq,numbers = zip(*sorted(zip(freq,numbers)))
        numbers = list(numbers)
        return numbers[len(numbers)-k:]



        