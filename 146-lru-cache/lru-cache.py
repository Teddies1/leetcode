class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = LLNode(0, 0)
        self.tail = LLNode(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        # add to head of doubly linkedlist
        next_node = self.head.next
        node.next = next_node
        next_node.prev = node
        node.prev = self.head
        self.head.next = node

    def delete(self, node):
        # remove from tail of doubly linkedlist
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # delete node from linkedlist and add to front of double linkedlist
        curr_node = self.cache[key]
        self.delete(curr_node)
        self.add(curr_node)
        return curr_node.value

    def put(self, key: int, value: int) -> None:
        # check if key in hashmap, if yes, delete from hashmap and DLL
        if key in self.cache:
            curr_node = self.cache[key]
            self.delete(curr_node)
            self.cache.pop(key)

        if len(self.cache) >= self.capacity:
            # remove lru node if exceed capacity
            lru_node = self.tail.prev
            self.delete(lru_node)
            self.cache.pop(lru_node.key)

        # add updated node to cache and linkedlist
        new_node = LLNode(key, value)
        self.cache[key] = new_node
        self.add(new_node)
'''
get in O(1): consider hashmap
put in O(1): consider double linked list

can have a hashmap that stores the keys, and value points to linkedlist nodes
linkedlist order is: left to right (least to most recently used)
when we use a put, we can check the hashmap if key in hashmap
    if cache hit, update key value
    also update the linkedlist by putting the node to the right
    if cache miss
    add key to hashmap and node to linked list
    if exceed capacity, delete left most node

when use get, check hashmap if key in hashmap
    if cache hit, return key
    update linkedlist by putting node to the right
    if cache miss, return -1
'''
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)