class TimeMap:
    def __init__(self):
        self.dict_moods = defaultdict(list)
        self.dict_times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_moods[key].append(value)
        self.dict_times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if not self.dict_times[key]:
            return ""
        else:
            if timestamp >= self.dict_times[key][-1]:
                return self.dict_moods[key][-1]
            elif timestamp < self.dict_times[key][0]:
                return ""

        timestamps = self.dict_times[key]
        l = 0
        r = len(timestamps) - 1
        while r >= l:
            cen = (r+l)//2
            if timestamps[cen] == timestamp:
                return self.dict_moods[key][cen]
            elif timestamps[cen] > timestamp:
                r = cen - 1
            else:
                l = cen + 1

        return self.dict_moods[key][r]











        
