class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        groups = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            groups.append(product)
        return groups                                
        