class Solution:
    def isValid(self, s: str) -> bool:
        #define queue = []
        queue = []
        #for each char in str
        for char in s:
            #if they are any of the open ones: push to queue
            if char == "(" or char == "[" or char == "{":
                queue.append(char)

            #if they are closed ones: pop queue and check if it is corresponding pair
            #if not return false
            elif char == ")":
                if not queue or queue.pop() != "(": return False
            elif char == "]":
                if not queue or queue.pop() != "[": return False
            elif char == "}":
                if not queue or queue.pop() != "{": return False
            
        #return true
        return not queue