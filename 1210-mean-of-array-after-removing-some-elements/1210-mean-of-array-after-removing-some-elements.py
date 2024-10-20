class Solution:
    def trimMean(self, arr: List[int]) -> float:
        l = len(arr)
        arr.sort()
        invalid = (l*5)//100
        
        return sum(arr[invalid:l-invalid]) / (l-(2*invalid))