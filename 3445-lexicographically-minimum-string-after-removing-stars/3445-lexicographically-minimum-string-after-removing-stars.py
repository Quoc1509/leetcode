class Solution:
    def clearStars(self, s: str) -> str:
        stk = []
        minStr = '~'
        heap = []
        mp = defaultdict(list)
        for i in range(len(s)):
            if s[i] == '*':
                c = heap[0]
                idx = mp[c].pop()
                stk[idx] = ''
                stk.append('')
                if not mp[c]:
                    heappop(heap)
            else:
                if not mp[s[i]]:
                    heappush(heap, s[i])
                mp[s[i]].append(i)
                stk.append(s[i])


        return ''.join(stk)