class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        i = 0
        for char in word:
            if char == '.':
                return self.dfs(curr, word, i)
            elif char not in curr.children:
                return False
            curr = curr.children[char]
            i += 1
        
        return curr.is_word

    def dfs(self, root, word, i):
        #base case means we searched everyting
        if i == len(word) and root.is_word:
            return True
        if i == len(word) and not root.is_word:
            return False

        #if our current letter is a .
        if word[i] == '.':
            for child in root.children:
                if self.dfs(root.children[child], word, i + 1) is True:
                    return True
            return False

        #our current letter is not a ., then check normally
        if word[i] in root.children:
            return self.dfs(root.children[word[i]], word, i + 1)
        else:
            return False
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)