class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = {}
        prev = ""
        curr = ""
        counter = 0
        ans = len(position)
        for i in range(len(position)):
            lst[position[i]] = speed[i]
        position.sort()
        
        while len(position) != 0:
            
            temp = position.pop()
            if prev == "":
                prev = (target-temp)/lst[temp]
            else:
                curr = (target-temp)/lst[temp]
                if prev >= curr:
                    counter += 1
                else:
                    prev = curr
            #print(prev, curr)
        print(counter)
        return(ans - counter)

        