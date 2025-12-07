# A trie is a tree-based data structure that organise information in a hierarchy
# while most of other structures are designed to manipulate data, trie is often used with strings it is used for storing words in a way which enables fast look-ups it stores characters at each node, it is very efficient for prefix matching in english language
# properties:
# - it is typically used to store or search strings in a space and time efficient way
# - any node in a trie can store non repetitive multiple characters
# - every node stores link of the next characters of the string
# - every node keep tracks of 'end of string'
#                               AB
#                            /       \
#                         I           AIM
#                       /           /  |  \
#                     RT          R    L   .
#                   /   \        /     \
#                 .      .      .       .
# or
#                              A
#                            /
#                         p
#                       /    \
#                     I       p
#                      \        \
#                       S.        L
#                        \         \
#                         .          E
#                                     \
#                                      .
# node always end with balnk node (i.e.,--> .)
# why we need it?
# to solve many standard problems in efficient way
# - spelling checker
# - auto completion
# insert a string in a trie:
# case 1: A trie is blank
# case 2: new string's prefix is common to another strings prefix
# case 3: new string's prefix is already present as complete string
# case 4: string to be inserted is already present in trie
# search string in a trie:
# case 1: string does not exist in trie
# case 2: string exist in trie
# case 3: string is a prefix of another string, but it does not exist in a trie
# delete a string from a trie:
# case 1: some other prefix of string is same as the one that we want to delete (eg. -> app and apple and api)
# case 2: the string is a prefix of another string. (eg. -> API, APIS)
# case 3: other string is a prefix of this string (eg. -> APIS, AP)
# case 4: not any node depends on string
#
class trie_node:
    def __init__(self):
        self.children = {}
        self.end_of_string = False
class trie:
    def __init__(self):
        self.root = trie_node()
    def insert_string(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = trie_node()  # so time and space complexity is O(m)
                current.children.update({ch:node})
            current = node
        current.end_of_string = True
        print('successfully inserted')
    def search_string(self, word):
        current_node = self.root
        for i in word:
            node = current_node.children.get(i)
            if node == None:
                return False  # so time and space complexity is O(m) and O(1)
            current_node = node
        if current_node.end_of_string == True:
            return True
        else:
            return False
def delete_string(root, word, index):
    ch= word[index]
    current_node = root.children.get(ch)
    can_this_node_be_deleted = False
    if len(current_node.children) > 1:
        delete_string(current_node, word, index + 1)
        return False
    if index == len(word) - 1:
        if len(current_node.children) >= 1:
            current_node.end_of_string = False
            return False
        else:
            root.children.pop(ch)
            return True
    if current_node.end_of_string == True:
        delete_string(current_node, word, index+1)
        return False

    can_this_node_be_deleted = delete_string(current_node, word, index+1)
    if can_this_node_be_deleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

new_trie = trie()
new_trie.insert_string("app")
new_trie.insert_string("appi")
delete_string(new_trie.root, "app" ,0)
print(new_trie.search_string("app"))
