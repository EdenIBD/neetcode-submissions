class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers)
        while numbers[i] + numbers[n-1] != target:
            if numbers[i] + numbers[n-1] > target:
                n -= 1
            elif numbers[i] + numbers[n-1] < target:
                i += 1
        
        return [i+1, n]
            


        