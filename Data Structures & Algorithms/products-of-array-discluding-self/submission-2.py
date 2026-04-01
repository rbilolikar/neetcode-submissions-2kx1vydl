class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = [1] * ( n + 1 )
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] * nums[i]

        suffix = [1] * (n + 1)
        for i in range(n, 0, -1):
            suffix[i - 1] = suffix[i] * nums[i-1]
        
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i + 1]

        return output