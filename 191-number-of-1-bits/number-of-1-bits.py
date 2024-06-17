class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
#         num = bin(n)[2:]
        
#         for nu in num:
#             if nu == "1":
#                 ans += 1
        while n:
            if ((1 & n) == 1):
                ans += 1;
            
            n >>= 1;
        return ans