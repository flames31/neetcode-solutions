class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in num_set:
            if num-1 in num_set:
                continue
            start = num
            while start in num_set:
                start += 1
            res = max(res, start-num)
        
        return res