def solution(s):
    
    if "p" not in s and "P" not in s and "y" not in s and "Y" not in s:
        return True
    if s.count("p")+s.count("P") == s.count("y")+s.count("Y"):
        return True
    else:
        return False