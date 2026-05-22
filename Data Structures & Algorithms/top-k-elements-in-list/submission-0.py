class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        sorted_freq = sorted(freq.items(), key= lambda x: x[1])
        arr = []
        for pair in sorted_freq[-k:]:
            arr.append(pair[0]) 
        return arr          