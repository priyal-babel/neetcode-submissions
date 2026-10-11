class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            buckets[frequency].append(num)

        output = []
        for frequency in range(len(nums),0,-1):
            for n in buckets[frequency]:
                output.append(n)

                if len(output)==k:
                    return output
