class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashset else False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
keyOp = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
valueOp = [[], [1], [2], [1], [3], [2], [2], [2], [2]]
output = []
for index, value in enumerate(keyOp):
    if value == "MyHashSet":
        obj = MyHashSet()
        output.append(None)
    elif value == "add":
        obj.add(valueOp[index][0])
        output.append(None)
    elif value == "contains":
        output1 = obj.contains(valueOp[index][0])
        output.append(output1)
    elif value == "remove" :
        obj.remove(valueOp[index][0])
        output.append(None)
print(output)



