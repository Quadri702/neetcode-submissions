class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1;
            else:
                freq[num] = 1;    
        sorted_freq = sorted(freq.items(), key=lambda item: item[1])  
        most = list(sorted_freq)[-1][0]
        return most