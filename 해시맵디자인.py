import collections
# 노드 클래스 생성
class ListNode :
    def __init__(self,key=None, value = None):
        self.key = key
        self.value = value 
        self.next = None 
        

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        

    def put(self, key: int, value: int) -> None:
        # 해시 테이블에 키값이 존재하지 않을때 
        index = key % self.size
        if self.table[index] is None :
            self.table[index] = ListNode(key, value)
            return 
        # 해시 테이블에 키값이 존재 할때 연결리스트로 연결
        p = self.table[index]
        
        while p :
            if p.key == key :
                p.value = value
                return
            if p.next is None :
                break
            p = p.next
        p.next = ListNode(key, value)
        
        
    def get(self, key: int) -> int:
        # 키값이 없을때 종료
        index = key % self.size 
        if self.table[index] is None :
            return -1 
        # 키값이 존재 할때 키 값 반환 
        p = self.table[index]
        
        while p :
            if p.key==key:
                return p.value
            p = p.next
        return -1 
        

    def remove(self, key: int) -> None:
        # 키값이 존재하지 않을때
        index = key % self.size
        if self.table[index] is None :
            return -1 
        # 키값이 존재 할때 맨앞노드 삭제시
        p = self.table[index]
        
        if p.key == key :
            self.table[index]=ListNode() if p.next is None else p.next 
            return -1 
        # 키값이 존째 할때 연결리스트 삭제시
        prev = p 
        
        while p :
            if p.key == key:
                prev.next = p.next
                return
            prev , p = p , p.next 