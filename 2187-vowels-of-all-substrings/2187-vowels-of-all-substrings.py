class Solution:
    def countVowels(self, word: str) -> int:
        
        vowels = {'a', 'e', 'o', 'i', 'u'}
        #dp[i] = sum of vowels of all substrings end at index i
        
        res = 0
        dp = [0] * (len(word)+1)
        for i in range(len(word)):
            if word[i] not in vowels:
                dp[i+1] = dp[i]
            else:
                dp[i+1] = dp[i]+i + 1

        return sum(dp)
