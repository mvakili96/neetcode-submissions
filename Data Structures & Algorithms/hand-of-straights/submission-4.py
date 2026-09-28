class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        dic = defaultdict(int)
        hand.sort()
        max_rep = 0
        for item in hand:
            dic[item] += 1
            max_rep = max(max_rep,dic[item])
        
        if max_rep > len(hand)//groupSize:
            return False
        
        groups = [[] for i in range(len(hand)//groupSize)]

        counter = 0
        while counter < len(hand):
            for i in range(dic[hand[counter]]):
                j = i
                while len(groups[j]) >= groupSize:
                    j += 1
                if not groups[j] or hand[counter] - groups[j][-1] == 1:
                    groups[j].append(hand[counter])
                else:
                    return False              
            counter += dic[hand[counter]]
        return True


        