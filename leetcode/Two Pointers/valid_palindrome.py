## Primary solution, string slicing
def isPalindrome2(s: str) -> bool:
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr +=c.lower()
    return newStr == newStr[::-1]  


## Overally bad solution using lists
def isPalindrome1(s: str) -> bool:
    strList = [x.lower() for x in s if x.isalnum()]
    start, end = 0, len(strList)-1
    while start < end:
        strList[start], strList[end] = strList[end], strList[start]
        start+=1
        end-=1
    print(strList)
    if strList == [x.lower() for x in s if x.isalnum()]:
        return True
    return False