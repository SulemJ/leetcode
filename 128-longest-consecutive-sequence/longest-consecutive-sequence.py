class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums=set(nums)
        dist=0
        for i in nums:
            if i-1 in nums: # we would find a better start than i 
                continue
            k=i+1
            while k in nums:
                k+=1
            dist=max(k-i, dist)
        return dist
            