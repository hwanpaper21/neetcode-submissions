class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ans = ""
        temp2 = ""
        temp=list(s)
        count = len(temp)-1

        while count != -1:
            if temp[count].isalpha() or temp[count].isalnum():
                temp2 += temp[count].lower()
            count -= 1

        for i in temp:
            if i.isalpha() or i.isalnum():
                ans += i.lower()

        print (ans, temp2)
        if ans == temp2:
            return True
        else:
            return False

