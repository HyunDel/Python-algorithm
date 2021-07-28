from typing import List

class Solution:
    # 투 포인트를 이용한 풀이 
    """
    def reverseString(self,s:List[str]) -> None:
        right, left = len(s) - 1 ,0
        while left < right :
              s[left],s[right]= s[right],s[left]
              left += 1
              right -= 1
    """
    #파이썬 기본기능을 이용한 풀이 
    def reverseString(self,s:List[str]) -> None:
        s.reverse()

    # s[:] = s[::-1] 트릭


    

    

      

    