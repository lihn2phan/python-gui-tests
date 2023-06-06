from sys import maxsize
class Group:
    def __init__(self, name, elem=None):
        self.name = name
        self.elem = elem
    def __repr__(self):
        return f"{self.elem}:{self.name}"

    def __eq__(self, other):
        t = (self.elem is None or other.elem is None or self.elem == other.elem)
        return t and self.name == other.name

    def elem_or_max(self):
        if self.elem:
            return int(self.elem)
        else:
            return maxsize