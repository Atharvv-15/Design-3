# 146. LRU Cache
class LRUCache:
    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map_ = {}
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self,curr):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
    
    def atToHead(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key not in self.map_:
            return -1
        else:
            node = self.map_[key]
            val = node.value
            self.removeNode(node)
            self.atToHead(node)
            return val
    
    def put(self, key: int, value: int) -> None:
        if key in self.map_:
            node = self.map_[key]
            node.value = value
            self.map_[key] = node
            self.removeNode(node)
            self.atToHead(node)
        else:
            if len(self.map_) == self.capacity:
                new_node = self.Node(key,value)
                tail_prev = self.tail.prev
                self.removeNode(tail_prev)
                self.map_.pop(tail_prev.key)
                self.atToHead(new_node)
                self.map_[key] = new_node   
            else:
                new_node = self.Node(key,value)
                self.atToHead(new_node)
                self.map_[key] = new_node
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)