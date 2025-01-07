class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if len(words[i]) > len(words[j]) or i == j:
                    continue
                check = False
                for k in range(len(words[j])):
                    # print(words[j], words[j][k:k+len(words[i])])
                    if words[j][k:k+len(words[i])] == words[i]:
                        res.append(words[i])
                        check = True
                        break
                if check:
                    break
        # print(res)
        return res
