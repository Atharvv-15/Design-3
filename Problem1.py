# 341. Flatten Nested List Iterator

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.stack.append(iter(nestedList))
        self.nextEl = None
    
    def next(self) -> int:
        return self.nextEl.getInteger()
        
    def hasNext(self) -> bool:
        while self.stack:
            try:
                current = next(self.stack[-1])
                if current.isInteger():
                    self.nextEl = current
                    return True
                else:
                    self.stack.append(iter(current.getList()))
            except StopIteration:
                self.stack.pop()
        return False