class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        current_nums = nums[:k]
        difference1 = current_nums[k-1] - current_nums[0]
        difference = difference1
        for i in range(k, len(nums)):
            difference2 = nums[i] - nums[i - k + 1]
            if difference2 < difference:
                difference = difference2
        return difference        
