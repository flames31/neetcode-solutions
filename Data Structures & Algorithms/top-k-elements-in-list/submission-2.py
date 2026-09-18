class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        freq = [[] for _ in range(len(nums)+1)]
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        for key, v in counts.items():
            freq[v].append(key)
        
        i = len(freq)-1
        ans = []
        while i > 0: 
            for j in range(len(freq[i])):
                if k > 0:
                    ans.append(freq[i][j])
                    k -= 1
                else:
                    return ans
            i -= 1
        
        return ans