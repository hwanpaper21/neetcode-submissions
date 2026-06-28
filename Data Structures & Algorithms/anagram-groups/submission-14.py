class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dit = {}
        lst1 = []
        tup1 = ()
        idx1 = []
        ans = []
        for i in strs:
            tmp = list(i)
            tmp.sort()
            tmp = "".join(tmp)
            lst1.append(tmp)
            if tmp in dit:
                pass
            else:
                dit[tmp] = tmp
        for j in dit:
            idx = 0
            for k in lst1:
                
                if j == k:
                    idx1.append(strs[idx])
                idx += 1
                print(idx)
            ans.append(idx1)
            idx1 = []
        return ans