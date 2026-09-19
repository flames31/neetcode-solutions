class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        num_dict = defaultdict(int)
        num_dict[0] = 1
        res = 0
        for num in nums:
            prefix += num
            if prefix - k in num_dict:
                res += num_dict[prefix-k]
            num_dict[prefix] += 1
        
        return res