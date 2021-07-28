from collections import deque

def Palimdrome(s: str) ->bool:
    # 리스트 방법을 통해서 풀이 
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
    # deque 방법을 통해서 풀이 
    strs =deque()
    
    for char in s :
        if char.isalnum():
            strs.append(char.lower())
            
    while len(strs) >1:
        if strs.popleft() != strs.pop():
            return False 
    
    return True 




