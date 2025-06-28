class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, password):
        node = self.root
        for char in password.strip():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def list_all(self):
        results = []

        def dfs(node, path):
            if node.end:
                results.append(''.join(path))
            for char, child in node.children.items():
                dfs(child, path + [char])

        dfs(self.root, [])
        return results

    def search(self, password):
        node = self.root
        for char in password.strip():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix.strip():
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def __str__(self):
        return '\n'.join(sorted(self.list_all()))
