class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        resList = []
        for num in digits:
            if len(resList) == 0:
                resList = letter[num].copy()
            else:
                tempList = []
                for i in resList:
                    temp = []
                    for j in letter[num]:
                        temp.append(i+j)
                    tempList += temp
                resList = tempList                       
        return resList
                


                
        

