class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def conquer(arr1, arr2):
            if not arr1:
                return arr2
            elif not arr2:
                return arr1
            i, j = 0, 0
            temp = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    temp.append(arr1[i])
                    i += 1
                elif arr1[i] > arr2[j]:
                    temp.append(arr2[j])
                    j += 1
                else:
                    temp.append(arr1[i])
                    temp.append(arr2[j])
                    i += 1
                    j += 1
            temp.extend(arr1[i:])
            temp.extend(arr2[j:])
            return temp

        def devide(arr):
            if len(arr) <= 1:
                return arr
            N = len(arr)//2
            l = devide(arr[:N])
            r = devide(arr[N:])
        
            return conquer(l, r)

        return devide(nums)
