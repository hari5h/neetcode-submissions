class Node:

    def __init__(self, val:int, key:int ):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]

            self.removeNode(node)
            self.addNode(node)

            return node.val 
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(value, key)
        if(key in self.map):
            self.removeNode(self.map[key])
        self.addNode(newNode)
        self.map[key] = newNode

        if(len(self.map) > self.capacity):
            lruNode = self.head.next
            del self.map[lruNode.key]
            self.removeNode(self.head.next)



    def addNode(self, newNode):
        prevNode = self.tail.prev
        
        prevNode.next = newNode
        self.tail.prev = newNode

        newNode.prev = prevNode
        newNode.next = self.tail

    def removeNode(self, currNode):
        prevNode = currNode.prev
        nextNode = currNode.next

        prevNode.next = nextNode
        nextNode.prev = prevNode


        
