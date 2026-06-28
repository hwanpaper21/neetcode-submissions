class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        counter = 0
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse = True))
        for item in count:
            ans.append(item)
            counter += 1
            if counter >= k:
                break
        return ans