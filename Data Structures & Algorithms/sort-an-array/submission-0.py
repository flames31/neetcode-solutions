class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        sorted_array = []

        while len(nums) > 0:
            sorted_array.append(heapq.heappop(nums))
        
        return sorted_array