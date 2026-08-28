class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_ = sorted(zip(position,speed), reverse=True)
        time_ref = -1
        counter = 0
        for pos,spd in sorted_:
            time = (target - pos)/spd
            if time > time_ref:
                time_ref = time
                counter += 1
        return counter


            