class TimeMap:

    def __init__(self):
        self.dic_mood = defaultdict(list)
        self.dic_time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic_mood[key].append(value)
        self.dic_time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic_mood:
            return ""

        nums = self.dic_time[key]
        left = 0
        right = len(nums) - 1

        if timestamp >= nums[-1]:
            return self.dic_mood[key][-1]
        if timestamp < nums[0]:
            return ""

        while left <= right:
            cen = (left + right) // 2

            if right == left and nums[cen] != timestamp:
                return self.dic_mood[key][cen-1]

            if nums[cen] < timestamp:
                left = cen + 1
            elif nums[cen] > timestamp:
                right = right - 1
            else:
                return self.dic_mood[key][cen]

        
