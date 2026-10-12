class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if left == right and nums[left] == target:
            return left
            
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[right] > target:
                right -= 1
            if nums[left] < target:
                left += 1
            
            
        return -1