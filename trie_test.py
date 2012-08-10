import unittest

from trie import Node
from trie import Trie

class TestTrie(unittest.TestCase):

    def test_init_node(self):
        node = Node('a')
        self.assertEqual(node.key, 'a')
        self.assertEqual(len(node.children), 0)

if __name__ == '__main__':
    unittest.main()
