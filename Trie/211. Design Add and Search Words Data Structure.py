class TrieNode:
    
    def __init__(self):
        self.node = defaultdict(TrieNode)
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            curr = curr.node[w]
        curr.isword = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for c in curr.node.values():
                        if dfs(i+1, c):
                            return True
                    return False
                else:
                    if c not in curr.node:
                        return False
                    curr = curr.node[c]
            
            return curr.isword

        return dfs(0,self.root)
