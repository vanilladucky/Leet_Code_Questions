class TrieNode:
    
    def __init__(self):
        self.nodes = defaultdict(TrieNode) 
        self.isword = False  

class Trie:

    def __init__(self):
        self.root=TrieNode() # The start of the node

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            curr = curr.nodes[w]
        curr.isword=True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.nodes:
                return False
            curr = curr.nodes[w]
        return curr.isword

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.nodes:
                return False
            curr = curr.nodes[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
