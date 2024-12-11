class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        temp = []
        for i in range(len(words)):
            temp.append((len(words[i]), i))
        temp.sort()
        
        mp = defaultdict(list)
        

        pre = [1] * len(words)
        def helper(s1, s2):
            count, j, i = 0, 0, 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    j += 1
                else:
                    count += 1
                if count >= 2:
                    return False
                i += 1
            return True

        for i in range(len(temp)):
            length = len(words[temp[i][1]])
            for j in mp[length-1]:
                check = helper(words[temp[i][1]], words[j])
                print(words[temp[i][1]], words[j], check)
                if check:
                    pre[temp[i][1]] = max(pre[temp[i][1]], pre[j] + 1)
            mp[length].append(temp[i][1])
        # print(pre)
        return max(pre)