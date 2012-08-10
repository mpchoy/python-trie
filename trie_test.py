import unittest

from trie import Node
from trie import Trie

class TestTrie(unittest.TestCase):

    def test_init_node(self):
        node = Node('a')
        self.assertEqual(node.key, 'a')
        self.assertEqual(len(node.children), 0)

    def test_init(self):
        trie = Trie()

    def test_insert_on_empty(self):
        trie = Trie()
        data = 'is for apple'
        trie.insert( 'a', data )
        self.assertIsNotNone(trie.get('a'))
        self.assertEqual(trie.get('a'), data)

    def test_insert_on_empty_long(self):
        trie = Trie()
        data = 'ripper X!'
        trie.insert( 'ab', data )
        self.assertIsNone(trie.get('a'))     # a is not in the dict
        self.assertIsNotNone(trie.get('ab')) # ab is
        self.assertEqual(trie.get('ab'), data)

    # TODO don't forget to try numbers


if __name__ == '__main__':
    unittest.main()
