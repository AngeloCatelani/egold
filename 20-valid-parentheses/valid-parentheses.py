class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap = {"}" : "{" , "]" : "[" , ")" : "("}
        
        for e in s:
            if e in hashmap:
                if stack and stack[-1] == hashmap[e]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(e)
        return True if not stack else False

    
        