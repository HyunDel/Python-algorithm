results =[] 
prev_elements = [] 
num = [1,2]
def dfs(elements):
            
            if len(elements) == 0 :
                results.append(prev_elements[:])
                
            for e in elements :
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
            
        
dfs(num)
print(results)

list = [1,2,3]
list.pop()
print(list)