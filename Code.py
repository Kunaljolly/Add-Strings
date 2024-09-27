class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        
        result = ''
        carry = 0
        
        for i in range(max_len - 1, -1, -1):
            n1 = int(num1[i])
            n2 = int(num2[i])
            total = n1 + n2 + carry
            result = str(total % 10) + result
            carry = total // 10
            
        if carry:
            result = str(carry) + result
            
        return result
