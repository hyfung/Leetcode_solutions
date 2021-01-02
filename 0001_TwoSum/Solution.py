class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force it, simple and elegant
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

                #         for i, i_v in enumerate(nums):
#             for j, j_v in enumerate(nums):
#                 if i > j:
#                     continue
#                 if i != j and i_v + j_v == target:
#                     return [i,j]
