class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for num in nums:
            unique_nums.add(num)
        if len(nums) != len(unique_nums):
            return True
        else:
            return False
        
        


        