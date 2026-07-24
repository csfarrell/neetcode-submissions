class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")" : "(", "]" : "[", "}" : "{"}
        # Go through each character in string
        for character in s:
            # If the character is a close to open bracket
            if character in brackets:
                # If the chosen bracket has a coresponding close/open, pop
                if stack and stack[-1] == brackets[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        if stack == []:
            return True
        else:
            return False
        