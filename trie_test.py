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

    def test_get_on_empty(self):
        trie = Trie()
        self.assertIsNone(trie.get('a'))
        self.assertIsNone(trie.get('ab'))
        self.assertIsNone(trie.get('xyz0'))

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

    def test_insert_on_empty_longer(self):
        trie = Trie()
        key = 'abstentia'
        data = 'Must be present to win'
        trie.insert( key, data )
        self.assertIsNone(trie.get('a'))
        self.assertIsNone(trie.get('absent'))
        self.assertEqual(trie.get(key), data)

    def test_insert_fork(self):
        trie = Trie()
        ab_data = 'ripper X!'
        ax_data = 'for chopping'
        trie.insert( 'ab', ab_data )
        trie.insert( 'ax', ax_data )
        self.assertIsNone(trie.get('a'))
        self.assertEqual(trie.get('ab'), ab_data)
        self.assertEqual(trie.get('ax'), ax_data)

    # TODO don't forget to try numbers


if __name__ == '__main__':
    unittest.main()
