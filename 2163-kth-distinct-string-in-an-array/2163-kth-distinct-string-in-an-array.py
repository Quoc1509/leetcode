class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        
        for key, item in count.items():
            if item == 1:
                k -= 1
            if k == 0:
                return key

        return ""