from collections import deque
import re

def Palimdrome(s: str) ->bool:
    # 리스트 방법을 통해서 풀이.
    """ 
    strs = []
    for char in s :
        if char.isalnum():
            strs.append(char.lower())
        

    while len(strs)>1:
        if strs.pop(0) != strs.pop():
            return False 

    return True
    """
    # Deque 방법을 통한 풀이.
    """
    # deque 방법을 통해서 풀이 
    strs =deque()
    
    for char in s :
        if char.isalnum():
            strs.append(char.lower())
            
    while len(strs) >1:
        if strs.popleft() != strs.pop():
            return False 
    
    return True 
    """

    # 슬라이싱 사용.

    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1]
    




