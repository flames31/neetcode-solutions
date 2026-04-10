class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [[] for _ in range(len(nums)+1)]
        ans = []

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for e in counts:
            l[counts[e]].append(e)

        for idx in range(len(nums), -1, -1):
            if k == 0:
                break

            if len(l[idx]) == 0:
                continue
            
            for e in l[idx]:
                ans.append(e)
                k -= 1
        
        return ans