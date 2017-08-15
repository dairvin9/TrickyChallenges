# exceeds time limit (not surpring, tbh). Could trim it down to a set I bet and make all of the z elements in there. or a map and keep track of the number of elements.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        seen = []
        old_i = None
        old_j = None
        old_k = None
        for i in range(len(nums)):
            if old_i == nums[i]:
                continue
            old_i = nums[i]    
            old_j = None
            for j in range(i+1,len(nums)):
                if old_j == nums[j]:
                    continue
                old_j = nums[j]
                old_k = None
                for k in range(j+1,len(nums)):
                    if old_k == nums[k]:
                        continue
                    old_k = nums[k]
                    if nums[i] + nums[j] + nums[k] == 0:
                       seen.append([nums[i],nums[j],nums[k]])
                          
        return seen      