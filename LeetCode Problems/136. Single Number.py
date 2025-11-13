class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
# First loop counts how many times each number appears.
        for s in nums:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
# Second loop finds the number that appears once
        for s in nums:
            if count[s]== 1:
                return s