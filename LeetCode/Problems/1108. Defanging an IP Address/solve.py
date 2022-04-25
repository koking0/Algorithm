class Solution:
    def defangIPaddr(self, address: str) -> str:
        address.replace('.', "[.]")
        return address
