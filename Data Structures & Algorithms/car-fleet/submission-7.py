class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_ = sorted(zip(position,speed), reverse=True)
        stack = [(target-sorted_[0][0])/sorted_[0][1]]
        for pos,spd in sorted_[1:]:
            time = (target - pos)/spd
            if time > stack[-1]:
                stack.append(time)
        return len(stack)


            