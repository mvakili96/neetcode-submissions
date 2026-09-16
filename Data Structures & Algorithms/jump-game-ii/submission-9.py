class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        farthest = 0
        current_end = 0
        step = 0
        for i in range(len(nums)):
            far_this = i + nums[i]
            if far_this > farthest:
                farthest = far_this

            if i == current_end:
                step += 1
                current_end = farthest

                if current_end >= len(nums) - 1:
                    return step

        return step


        