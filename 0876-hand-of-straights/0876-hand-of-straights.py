class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        count = Counter(hand)
        hand = list(count.keys())
        hand.sort()
        i = 0
        while count:
            if hand[i] not in count:
                i += 1
                continue
            cur, num = 0, hand[i]
            while cur < groupSize:
                if num not in count: return False
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
                cur += 1
                num += 1
        # print(temp)
        return True