import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = ["hello", "hell", "help", "hero", "her"]
        for word in self.words:
            self.trie.insert(word)

    def test_search_existing(self):
        for word in self.words:
            self.assertTrue(self.trie.search(word))

    def test_search_non_existing(self):
        self.assertFalse(self.trie.search("he"))
        self.assertFalse(self.trie.search("helmet"))

    def test_starts_with(self):
        self.assertTrue(self.trie.starts_with("he"))
        self.assertTrue(self.trie.starts_with("hel"))
        self.assertFalse(self.trie.starts_with("ho"))

    def test_list_all(self):
        listed = sorted(self.trie.list_all())
        expected = sorted(self.words)
        self.assertEqual(listed, expected)

    def test_str_contains_all_words(self):
        tree_str = str(self.trie)
        for word in self.words:
            self.assertIn(word[0], tree_str)  # First char should definitely be there
        for word in self.words:
            self.assertIn(word, tree_str)
if __name__ == '__main__':
    unittest.main()