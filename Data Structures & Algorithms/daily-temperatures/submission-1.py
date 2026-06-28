class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        templst = temperatures.copy()
        templst.reverse()
        counter = 0
        templst2 = []
        seq = 0
        ans = []
        flag = 'N'
        for i in range(len(temperatures)):
            counter = 0
            flag = 'N'
            seq = i + 1
            templst2 = templst.copy()
            templst2 = templst2[0:len(templst2)-seq]
            print(templst2)
            while len(templst2) != 0:
                counter += 1
                if templst2.pop() > temperatures[i]:
                    ans.append(counter)
                    flag = 'Y'
                    break
            if flag == 'N':
                ans.append(int(0))

        return ans