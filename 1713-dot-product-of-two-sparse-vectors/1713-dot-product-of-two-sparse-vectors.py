class SparseVector:
    def __init__(self, nums: List[int]):
        self.mp = {}
        for i, e in enumerate(nums):
            if e != 0:
                self.mp[i] = e

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        mp1 = self.mp
        mp2 = vec.mp
        if len(mp1) > len(mp2):
            mp1, mp2 = mp2, mp1
        res = 0
        for key, item in mp1.items():
            if key in mp2:
                res += (item * mp2[key])
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)