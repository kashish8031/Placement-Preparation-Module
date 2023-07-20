class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        while i < n and s[i] == ' ': 
            i += 1

        positive = 0
        negative = 0

        if s[i] == '+':
            positive += 1  
            i += 1

        if s[i] == '-':
            negative += 1  
            i += 1

        ans = 0.0

        while i < n and '0' <= s[i] <= '9':
            ans = ans * 10 + (ord(s[i]) - ord('0'))  
            i += 1

        if negative > 0:  
            ans = -ans

        if positive > 0 and negative > 0:  
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if ans > INT_MAX:  
            ans = INT_MAX

        if ans < INT_MIN:  
            ans = INT_MIN

        return int(ans)