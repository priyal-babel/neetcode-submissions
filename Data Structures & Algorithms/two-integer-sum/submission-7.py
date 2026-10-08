class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dic:
                j = dic[complement][-1]
                if i != j:
                    return [i, j]

        