from typing import List
from collections import defaultdict


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.dead = set()
        self.edges = defaultdict(list)

    def birth(self, parentName: str, childName: str) -> None:
        self.edges[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = list()

        def preorder(name: str) -> None:
            if name not in self.dead:
                ans.append(name)
            if name in self.edges:
                for childName in self.edges[name]:
                    preorder(childName)

        preorder(self.king)
        return ans
