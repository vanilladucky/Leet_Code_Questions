class TrieNode:
    
    def __init__(self):
        self.nodes = defaultdict(TrieNode) 
        self.isword = False  

class Trie:

    def __init__(self):
        self.root=TrieNode() # The start of the node
        self.number_of_words = 0

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            curr = curr.nodes[w]
        curr.isword=True
        self.number_of_words += 1

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.nodes:
                return False
            curr = curr.nodes[w]
        return curr.isword

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res=[]
        obj = Trie()
        for w in words:
            obj.insert(w)
        curr = obj.root
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.backtrack(i,j,board,curr,"", res, obj)
                
        return res
                
    def backtrack(self, i, j, board, curr, path, res, obj):
        if not curr or obj.number_of_words==0:
            return        
        if curr.isword:
            res.append(path)
            curr.isword=False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        letter = board[i][j]
        curr=curr.nodes.get(letter)
        if not curr:
            return
        board[i][j] = "#" # Same letter cannot be used more than once
        self.backtrack(i-1,j,board,curr,path+letter,res,obj)
        self.backtrack(i+1,j,board,curr,path+letter,res,obj)
        self.backtrack(i,j-1,board,curr,path+letter,res,obj)
        self.backtrack(i,j+1,board,curr,path+letter,res,obj)
        board[i][j] = letter
