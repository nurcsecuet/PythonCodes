class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i<len(nums):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
            else:
                i += 1
        print(nums)