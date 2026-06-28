class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Analst = {}
        ans = []
        x = []
        counter = 0
        for i in strs:
            temp = list(i)
            temp.sort()
            temp = "".join(temp)
            if temp in Analst:
                Analst[temp] = str(Analst[temp]) + "," + str(counter)
            else:
                Analst[temp] = counter
            counter += 1

        for j in Analst:
            if "," in str(Analst[j]):
                lst = Analst[j].split(",")
                print(lst)
                for k in lst:
                    x.append(strs[int(k)])
            else:
                x.append(strs[int(Analst[j])])
            ans.append(x)
            x = []
        return ans


            