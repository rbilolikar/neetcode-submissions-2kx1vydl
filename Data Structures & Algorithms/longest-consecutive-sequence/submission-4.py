class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        mySet = set(nums)
        
        for num in mySet:
            if num - 1 not in mySet: #start of a sequence
                length = 1
                while num + 1 in mySet:
                    length += 1
                    num += 1
                longest = max(longest, length)
        return longest
            

