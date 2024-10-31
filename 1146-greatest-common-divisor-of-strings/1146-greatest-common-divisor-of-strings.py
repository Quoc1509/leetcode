class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def helper(s):
            A = [0] * len(s)
            for i in range(1, len(s)):
                j = A[i-1]
                while j > 0 and s[i] != s[j]:
                    j = A[j-1]
                if s[i] == s[j]:
                    A[i] = j + 1
            return A
        
        res1 = helper(str1)
        res2 = helper(str2)
        print(res1, res2)
        len1 = len(str1)-res1[-1]
        len2 = len(str2)-res2[-1]

        if str1[:len1] != str2[:len2] or len(str1)%len1 != 0 or len(str2)%len2 != 0:
            return ''

        temp1 = len(str1)//len1
        temp2 = len(str2)//len2
        temp = math.gcd(temp1, temp2)

        return str2[:len2*temp]

            