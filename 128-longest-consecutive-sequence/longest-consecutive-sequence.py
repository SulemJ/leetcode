class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums=list(set(nums))
        if len(nums)==1: return 1
        nums.sort()
        dist=0
        l,r=0,1
        while r < len(nums):
            if nums[r]-nums[r-1]==1:
                r+=1
            else:
                l=r
                r+=1
            dist=max(r-l, dist)
        return dist
            