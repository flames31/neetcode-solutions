class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        se = set()
        for num in nums:
            se.add(num)

        ans = 0

        for num in nums:
            if num - 1 in se:
                continue

            count = 0  
            while num in se:
                count += 1
                num += 1

            ans = max(ans, count)
		
        return ans