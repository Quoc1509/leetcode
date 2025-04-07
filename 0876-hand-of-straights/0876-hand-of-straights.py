class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        res = 0
        hand.sort()
        while hand:
            while hand and hand[-1] not in count:
                hand.pop()
            if hand:
                num = hand[-1]
                c = 0
                while c < groupSize and num in count:
                    count[num] -= 1
                    c += 1
                    if count[num] == 0:
                        del count[num]
                    num -= 1
                if c < groupSize:
                    return False

        return True
                    

