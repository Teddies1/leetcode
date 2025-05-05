class PFNode:
    def __init__(self):
        self.hashmap = {}
        self.marker = False

class PrefixTree:
    def __init__(self):
        self.tree = PFNode()
        self.ans = []

    def insert(self, val):
        curr = self.tree
        val = str(val)
        for c in val:
            if c not in curr.hashmap:
                curr.hashmap[c] = PFNode()
            curr = curr.hashmap[c]
        curr.marker = True
    
    def retrieve(self, node, state):
        if node.marker:
            self.ans.append(int(state))
        
        for k, v in node.hashmap.items():
            self.retrieve(v, state + k)
        return


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        prefix_tree = PrefixTree()

        for i in range(1, n+1):
            prefix_tree.insert(i)
        
        prefix_tree.retrieve(prefix_tree.tree, "")

        return prefix_tree.ans

'''
idea is to create a 'trie' for numbers
create a node called Node
each node contains a hashmap, which contains digits from 0 to 9
each node also contains a marker, which is true when there is an associated value stored in that node digit

each key in the hashmap points to another node, which contains the next digit of a number
'''
