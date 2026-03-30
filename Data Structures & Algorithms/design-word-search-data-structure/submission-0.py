class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.endOfWord
            
            c = word[i]

            if c == ".":
                for child in node.children:
                    if child and dfs(child, i+1):
                        return True
                return False
            
            idx = ord(c) - ord("a")
            if not node.children[idx]:
                return False

            return dfs(node.children[idx], i+1)

        return dfs(self.root, 0)