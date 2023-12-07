class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]
        
    def hashcode(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hashcode(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
         
    def get(self, key: int) -> int:
        cur = self.map[self.hashcode(key)].next
        while cur and cur.key != key:
            cur = cur.next
        if cur:
            return cur.val
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hashcode(key)]
        while cur.next and cur.next.key != key:
            cur = cur.next
        if cur and cur.next:
            cur.next = cur.next.next

#Input
keyOPs= ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
valueOps =[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
obj = MyHashMap()
output = []
#[null, null, null, 1, -1, null, 1, null, -1]
for index, value in enumerate(keyOPs):
    if value == "MyHashMap":
        obj = MyHashMap()
        output.append(None)
    elif value == "get":
        output1 = obj.get(valueOps[index][0])
        output.append(output1)
    elif value == "put":
        obj.put(valueOps[index][0], valueOps[index][1])
        output.append(None)
    elif value == "remove":
        obj.remove(valueOps[index][0])
        output.append(None)
print(output)