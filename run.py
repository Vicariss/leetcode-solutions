
# class Color():
#     def __init__(self, red, green, blue):
#         self._red, self._green, self._blue = red, green, blue

#     def __str__(self):
#         return f'{self._red, self._green, self._blue}'

#     @classmethod
#     def by_name(cls, color_name):
#         color_defs = {'white':(255,255,255), 'red':(255,0,0),
#                        'green':(0,255,0),'blue':(0,0,255)}
#         return cls(*color_defs[color_name])

# red = Color(255,0,0)
# red2 = Color.by_name('green')

# print(red, red2)




## Overally bad solution
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
 
