class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        N = 10**9+7
        # res = [0] * n
        # res[0] = 1
        # for i in range(n):
        #     index = i+delay
        #     while index < i+forget and index < n:
        #         res[index] += res[i]
        #         index += 1
        # return sum(res[n-forget:])%N
        prefix = [0] * n
        dp = [0] * n
        dp[0] = 1

        for i in range(n):
            if i >= forget:
                dp[i] = prefix[i-delay]-prefix[i-forget]
            elif i >= delay:
                dp[i] = prefix[i-delay]
            prefix[i] = (prefix[i-1] if i > 0 else 0) + dp[i]
        print(prefix)
        return (prefix[-1] - (prefix[-forget-1] if n-forget-1 >= 0 else 0))%N

