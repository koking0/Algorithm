class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = set()

    def add(self, key: int) -> None:
        self.dic.add(key)

    def remove(self, key: int) -> None:
        try:
            self.dic.remove(key)
        except KeyError:
            return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.dic


if __name__ == '__main__':
    # Your MyHashSet object will be instantiated and called as such:
    obj = MyHashSet()
    obj.add(key)
    obj.remove(key)
    param_3 = obj.contains(key)
