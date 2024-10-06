class Solution:
    def isValid(self, s: str) -> bool:
        # using stack DS because we are popping out from first
        # hashmap act like objects or dict to store key value pairs where keys are closing brackets
        # output-> boolean

        stack=[]
        closingToOpen = {"}" : "{" , "]" : "[" , ")":"("}
        for c in s: #checking each bracket from s
            if c in closingToOpen: # then that bracket is present in dict
                if stack and stack[-1] == closingToOpen[c]: # can not add closing bracket to stack so checking in hashmap. stack and stack's last element is equal to closingbracket's key
                    stack.pop() # then pop it out
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        # time complexity - O(n)
        # space - O(n)
            