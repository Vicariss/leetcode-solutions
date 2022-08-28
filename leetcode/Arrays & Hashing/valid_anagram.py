# Valid Anagram

def isAnagram(s: str, t: str) -> bool:
    # strings cant have distinct length
    if len(s) != len(t):
        return False
    sCount, tCount = {}, {}
    for charIndex in range(len(s)):  # len is the same so it can operate on two strings
        sCount[s[charIndex]] = 1 + sCount.get(s[charIndex], 0)
        tCount[t[charIndex]] = 1 + tCount.get(t[charIndex], 0)
    # check if character counts match
    for char in sCount:
        if sCount.get(char) != tCount.get(char):
            return False
    return True


def isAnagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


    
    
