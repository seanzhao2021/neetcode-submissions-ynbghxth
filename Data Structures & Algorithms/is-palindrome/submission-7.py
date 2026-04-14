class Solution:
    def isPalindrome(self, s: str) -> bool:
        #define left right pointers
        l, r = 0, len(s) - 1

        #while left does not cross right pointer
        while(l < r):
            #if pointers on non alphanumerical char, move left up or right down
            #while loop to do increment/decrement until not pointing to spce or num
            while(not s[l].isalnum() or not s[r].isalnum()):
                
                if not s[l].isalnum(): l += 1
                if not s[r].isalnum(): r -= 1

                print(l, r)
                if r < 0 or l > len(s): return True
                

            #check if char.tolowercase is equal for both poitners
            #return false if not
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
            
        #return true
        return True