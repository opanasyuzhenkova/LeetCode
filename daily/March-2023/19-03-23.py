# 211. Design Add and Search Words Data Structure

# Trie Version

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_word = False


# class WordDictionary:
#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word: str) -> None:
#         current_node = self.root
#         for character in word:
#             cur_node = cur_node.children.setdefault(character, TrieNode())
#         cur_node.is_word = True

#     def search(self, word: str) -> bool:
#         def dfs(node, index):
#             if index == len(word):
#                 return node.is_word
#             if word[index] == ".":
#                 for child in node.children.values():
#                     if dfs(child, index + 1):
#                         return True
#             if word[index] in node.children:
#                 return dfs(node.children[word[index]], index + 1)
            
#             return False
        
#         return dfs(self.root, 0)



from collections import defaultdict 

class WordDictionary:
        def __init__(self):
            self.words = defaultdict(list)


        def addWord(self, word: str) -> None:
            self.words[len(word)].append(word)
            print(self.words)


        def search(self, word: str) -> bool:
            n = len(word)
            if '.' in word:
                for w in self.words[n]:
                    if all(word[i] in (w[i], '.') for i in range(n)):
                        return True
                else: 
                    return False

            return word in self.words[n]
        
obj = WordDictionary()
obj.addWord('word')
obj.addWord('.at')
param_2 = obj.search('words')
obj.addWord('.dt')
param_2 = obj.search('.at')
print(param_2)