from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = collections.defaultdict(int)
        for i, num in enumerate(nums):
            res = target - num
            if res in seen:
                return list([seen[res], i])
            seen[num] = i

