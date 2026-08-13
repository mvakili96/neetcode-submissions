class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        fleet = 1
        for i in range(len(position)):
            times.append((target-position[i])/speed[i])
        
        sorted_position, sorted_time = zip(*sorted(zip(position, times)))
        max_time = sorted_time[-1]
        for i in range(len(sorted_time)-2,-1,-1):
            if sorted_time[i] > max_time:
                max_time = sorted_time[i]
                fleet += 1
        
        return fleet

            