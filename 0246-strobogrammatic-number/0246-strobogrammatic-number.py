class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        for i in range((len(num)//2)+1):
            print(i, len(num)-i-1)
            if num[i] == num[len(num)-i-1]:
                if num[i] == '1' or num[i] == '0' or num[i] == '8':
                    continue
            elif (num[i] == '6' and num[len(num)-i-1] == '9') or (num[i] == '9' and num[len(num)-i-1] == '6'):
                continue
            return False
        return True