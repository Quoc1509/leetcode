class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = defaultdict(int)
        monoStack = []
        for num in nums2:
            while monoStack and monoStack[-1] < num:
                n = monoStack.pop()
                mp[n] = num
            monoStack.append(num)
        res = []
        
        for num in nums1:
            if mp[num] == 0:
                res.append(-1)
            else:
                res.append(mp[num])
        return res

            