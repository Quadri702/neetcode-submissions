class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array = []
        for i in range(2):
            for num in nums:
                array.append(num)
        return array        