class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

    def insert(self, word: str) -> None:
        self.insert_helper(word, 0)
        
    def insert_helper(self, word, index):
        if word[index] not in self.children:
            self.children[word[index]] = Trie()
        if index == len(word) - 1:
            self.children[word[index]].word = True
            return
        self.children[word[index]].insert_helper(word, index+1)
        
    def search(self, word: str) -> bool:
        if not word: return False
        return self.search_helper(word, 0)
        
    def search_helper(self, word, index):
        if word[index] not in self.children:
            return False
        if index == len(word) - 1:
            return self.children[word[index]].word
        return self.children[word[index]].search_helper(word, index+1)
                           
    def startsWith(self, prefix: str) -> bool:
        return self.startsWith_helper(prefix, 0)
    
    def startsWith_helper(self, word, index):
        if word[index] not in self.children:
            return False
        if index == len(word) - 1:
            return True
        return self.children[word[index]].startsWith_helper(word, index+1)
       
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        trie, bucket = Trie(), defaultdict(list)
        for word in words:
            trie.insert(word)
            bucket[len(word)].append(word)

        @cache
        def chain(word):
            if not word:
                return 1
                
            candidates = []
            for index in range(1, len(word)+1):
                wprd = word[:index-1] + word[index:]
                candidates.append(wprd)
            
            longest = 1
            for candidate in candidates:
                if trie.search(candidate):
                    longest = max(1 + chain(candidate), longest)
            return longest

        longest = 1
        for bvcket in range(max(bucket),1,-1):
            for word in bucket[bvcket]:
                longest = max(chain(word), longest)
        return longest
