class SparseVector:
    def __init__(self, nums: List[int]):
        self.arr = []
        for i, e in enumerate(nums):
            if e != 0:
                self.arr.append((i, e))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        arr1 = self.arr
        arr2 = vec.arr
        i1, i2 = 0, 0
        res = 0
        while i1 < len(arr1) and i2 < len(arr2):
            if arr1[i1][0] == arr2[i2][0]:
                res += (arr1[i1][1]*arr2[i2][1])
                i1 += 1
                i2 += 1
            elif arr1[i1][0] > arr2[i2][0]:
                i2 += 1
            else: i1 += 1
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)