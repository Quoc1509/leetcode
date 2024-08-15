class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = [0, 0]
        for bill in bills:
            if bill == 5:
                money[0] += 1
                continue

            if money[0] == 0 and money[1] == 0: return False
            if bill == 10:
                if money[0] == 0: return False
                money[1] += 1
                money[0] -= 1
            else:
                if money[0] < 3 and money[1] < 1: return False
                if money[0] == 0: return False
                if money[1]: 
                    money[1] -= 1
                    money[0] -= 1
                else:
                    money[0] -= 3

        return True
                

                
        