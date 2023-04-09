"""
Write a union find data structure that can be used to efficiently find the union of two sets of integers.
"""
class UnionFind:
    def __init__(self):
        self.parent = {}

    def createSet(self, value):
        self.parent[value] = value

    def find(self, value):
        if value not in self.parent:
            return None
        while value != self.parent[value]:
            value = self.parent[value]
        return value

    def union(self, valueOne, valueTwo):
        rootOne = self.find(valueOne)
        rootTwo = self.find(valueTwo)
        if rootOne is None or rootTwo is None:
            return
        if rootOne != rootTwo:
            self.parent[rootTwo] = rootOne


if __name__ == "__main__":
    union = UnionFind()
    union.createSet(1)
    union.createSet(2)
    union.createSet(3)
    union.createSet(4)
    union.createSet(5)
    union.createSet(6)
    union.createSet(7)
    union.createSet(8)
    union.createSet("hello")

    print(union.find(1))
    print(union.find(2)) 
    print(union.find("hello"))
    union.union(1, 2)
    [print(i) for i in union.parent.values()] # 1, 1, 3, 4, 5, 6, 7, 8
