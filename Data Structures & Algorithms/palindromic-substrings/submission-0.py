class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrome(l, r):
            if r - l == 2: total = 1
            else: total = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                r += 1
                l -= 1
            return total
        
        ans = 0
        for i in range (len(s)):
            ans += palindrome(i, i+1)
            ans += palindrome(i - 1, i + 1)
        return ans