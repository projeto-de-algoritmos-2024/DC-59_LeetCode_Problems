class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        def decode(num):
            ans = 0
            for i in num:
                ans = ans*10 +(ord(i) - ord('0'))
            return ans

        def encode(s):
            news = ''
            while s:
                a = s % 10
                s = s // 10
                news = chr(ord('0') + a) + news
            return news
        
        return encode(decode(num1)*decode(num2))

######### FUNÇÕES PARA RODAR LOCAL FORA DO LEETCODE ############
solution = Solution()
# Example 1
num1, num2 = "2", "3"
output = solution.multiply(num1, num2)
print(f"Input: num1 = \"{num1}\", num2 = \"{num2}\"\nOutput: \"{output}\"\n")

# Example 2
num1, num2 = "123", "456"
output = solution.multiply(num1, num2)
print(f"Input: num1 = \"{num1}\", num2 = \"{num2}\"\nOutput: \"{output}\"\n")