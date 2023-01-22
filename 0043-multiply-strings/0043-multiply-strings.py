class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=[]
        n2=[]
        first=0
        second=0
        for i in num1:
            n1.append(ord(i)-ord('0'))
        for i in num2:
            n2.append(ord(i)-ord('0'))
        
        for i in range(len(n1)):
            first+=n1[len(n1)-i-1]*10**i
        for i in range(len(n2)):
            second+=n2[len(n2)-i-1]*10**i
        return str(first*second)