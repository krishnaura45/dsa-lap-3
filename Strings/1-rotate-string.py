# first thought sol -> 0 ms (>100%), 19.38 MB (>15.24%)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)==len(goal):
            temp=s
            s=s+' '
            i=0
            while s[i]!=' ':
                temp+=s[i]
                if goal==temp[-len(goal):]:
                    return True
                i+=1
        return False
    
# Memory efficient -> 19.25 MB (>51.56%)
class Solution2:
# Strings must be of the same length to be rotations of each other
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False  
        doubled_s = s + s  # Concatenate s with itself
        return goal in doubled_s  # Check if goal is a substring of s + s