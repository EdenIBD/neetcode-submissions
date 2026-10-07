class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        array = []
        for num in nums:
            if num not in frequency_dict.keys():
                frequency_dict[num] = 1
            else:
                frequency_dict[num] += 1

        sorted_dict = sorted(frequency_dict.items(), key = lambda x:x[1], reverse = True)

        for tuple in sorted_dict[:k]:
            array.append(tuple[0])

        return array
            
        
        

