class Solution:
    def countPrimes(self, n: int) -> int:
        if n is None:
            return 0
        if n <= 2:
            return 0

        s = self.sieve(n)
        count = 0
        for i in range(len(s)):
            if s[i] == True:
                count += 1

        return count

    def sieve(self, n):
        array = [True] * (n)
        array[0] = False
        array[1] = False

        for i in range(n):
            if array[i] == True and i * i < n:
                for j in range(i*i, n, i):
                    array[j] = False

        return array