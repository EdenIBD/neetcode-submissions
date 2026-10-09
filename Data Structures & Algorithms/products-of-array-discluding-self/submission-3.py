class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        for t in range(len(nums)):
            product *= nums[t]

        for i in range(len(nums)):
            if nums[i] == 0:
                product_without_zero = 1
                for j in range(len(nums)):
                    if j != i:
                        product_without_zero *= nums[j]
                output.append(product_without_zero)
            else:
                output.append(int(product/nums[i]))


        return output

