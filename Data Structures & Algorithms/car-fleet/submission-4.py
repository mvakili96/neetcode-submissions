class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position,speed = zip(*sorted(zip(position,speed)))
        position = list(position)
        speed = list(speed)
        counter = 1
        for i in range(len(position)-2,-1,-1):
            if speed[i] <= speed[i+1]:
                counter += 1
            else:
                if (target - position[i])/speed[i] > (target - position[i+1])/speed[i+1]:
                    counter += 1
                else:
                    position[i] = position[i+1]
                    speed[i] = speed[i+1]
        
        return counter


            