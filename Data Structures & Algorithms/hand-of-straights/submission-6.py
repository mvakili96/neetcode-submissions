class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        dic = defaultdict(int)
        hand.sort()

        for item in hand:
            dic[item] += 1

        for num in hand:
            if dic[num] > 0:
                for counter in range(num,num+groupSize):
                    if dic[counter] > 0:
                        dic[counter] -= 1
                    else:
                        return False
        return True


        