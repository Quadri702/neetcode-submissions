class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    arr.append(i)
                    nums2.remove(j)
                    break
        return arr            