class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        temp = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                temp[i] = 1
        c = defaultdict(int)
        c[0] = 1
        total,res = 0, 0
        for val in temp:
            total += val
            mod_value = total % modulo
            
            # Calculate the required target value
            target_value = (mod_value - k + modulo) % modulo
            
            # Add the count of such prefix sums found in the prefix_count map
            res += c[target_value]
            
            # Update the prefix_count map with the current mod value
            c[mod_value] += 1
        
        return res