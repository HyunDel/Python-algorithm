from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs(index, path):
            # path길이와, digits 길이가 같을때는 문자열 추가 
            if len(path) == len(digits):
                result.append(path)
                return 
            # 자릿수 단위 반복
            for i in range(index,len(digits)):
                # 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i+1,path+j)
            
        # 예외처리 
        if not digits :
            return [] 
        
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        dfs(0,"")
        
        return result 