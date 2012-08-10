import unittest

from trie import Node
from trie import Trie

class TestTrie(unittest.TestCase):
    # TODO don't forget to try numbers

    def test_init_node(self):
        node = Node()
        self.assertIsNone(node.data)
        self.assertEqual(len(node.children), 0)

    def test_has_data(self):
        node = Node()
        self.assertFalse(node.has_data())
        node.data = 1
        self.assertTrue(node.has_data())

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
        key = 'absentia'
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

    def test_insert_overlap(self):
        trie = Trie()
        key_a = 'a'
        key_at = 'at'
        key_ate = 'ate'
        data_a = 'is for apple'
        data_at = '@'
        data_ate = 'a verb in past tense'
        trie.insert( key_a, data_a )
        trie.insert( key_at, data_at )
        trie.insert( key_ate, data_ate )
        self.assertEqual(trie.get(key_a), data_a)
        self.assertEqual(trie.get(key_at), data_at)
        self.assertEqual(trie.get(key_ate), data_ate)

    def test_remove_on_empty(self):
        trie = Trie()
        self.assertIsNone(trie.remove('a'))
        self.assertIsNone(trie.remove('z'))
        self.assertIsNone(trie.remove('abracadabra'))

    def test_remove_1(self):
        trie = Trie()
        key = 'a'
        data = 123
        trie.insert( key, data )
        self.assertIsNotNone(trie.get(key))
        self.assertEqual(trie.remove(key), data)
        self.assertIsNone(trie.get(key))

    def test_remove_long(self):
        trie = Trie()
        key = 'abc'
        data = 123
        trie.insert( key, data )
        self.assertIsNotNone(trie.get(key))
        self.assertEqual(trie.remove(key), data)
        self.assertIsNone(trie.get(key))

    def test_remove_one_but_not_both(self):
        trie = Trie()
        key1 = 'abc'
        key2 = 'abd'
        data1 = 123
        data2 = 987
        trie.insert( key1, data1 )
        trie.insert( key2, data2 )
        self.assertEqual(trie.remove(key1), data1)
        self.assertIsNone(trie.get(key1))
        self.assertEqual(trie.get(key2), data2)

    def test_remove_overlap(self):
        trie = Trie()
        key_a = 'a'
        key_at = 'at'
        key_ate = 'ate'
        data_a = 'is for apple'
        data_at = '@'
        data_ate = 'a verb in past tense'
        trie.insert( key_a, data_a )
        trie.insert( key_at, data_at )
        trie.insert( key_ate, data_ate )

        trie.remove(key_at)
        self.assertIsNone(trie.get(key_at))

        self.assertEqual(trie.get(key_a), data_a)
        self.assertEqual(trie.get(key_ate), data_ate)

        trie.remove(key_a)
        self.assertIsNone(trie.get(key_a))

        self.assertEqual(trie.get(key_ate), data_ate)

    def test_match_prefix_0(self):
        trie = Trie()

        matches = trie.match_prefix('a')
        self.assertEqual(len(matches), 0)

        matches = trie.match_prefix('z')
        self.assertEqual(len(matches), 0)

        matches = trie.match_prefix('abracadabra')
        self.assertEqual(len(matches), 0)

    def test_match_prefix_1(self):
        trie = Trie()
        key_a = 'a'
        data_a = 0

        trie.insert( key_a, data_a )

        matches = trie.match_prefix('a')
        self.assertEqual(len(matches), 1)
        self.assertTrue(key_a in matches)

        matches = trie.match_prefix('z')
        self.assertEqual(len(matches), 0)

        matches = trie.match_prefix('abracadabra')
        self.assertEqual(len(matches), 0)

    def test_match_prefix_2(self):
        trie = Trie()
        key_a = 'a'
        key_at = 'at'
        key_ate = 'ate'
        data_a = 'is for apple'
        data_at = '@'
        data_ate = 'a verb in past tense'
        trie.insert( key_a, data_a )
        trie.insert( key_at, data_at )
        trie.insert( key_ate, data_ate )

        matches = trie.match_prefix('at')
        self.assertEqual(len(matches), 2)
        self.assertTrue(key_ate in matches)
        self.assertTrue(key_at in matches)

        matches = trie.match_prefix('a')
        self.assertEqual(len(matches), 3)
        self.assertTrue(key_ate in matches)
        self.assertTrue(key_at in matches)
        self.assertTrue(key_a in matches)

    def test_match_prefix_3(self):
        trie = Trie()
        key_a = 'a'
        key_at = 'at'
        key_absent = 'absent'
        data_a = 'is for apple'
        data_at = '@'
        data_absent = ''
        trie.insert( key_a, data_a )
        trie.insert( key_at, data_at )
        trie.insert( key_absent, data_absent )

        matches = trie.match_prefix('a')
        self.assertEqual(len(matches), 3)
        self.assertTrue(key_a in matches)
        self.assertTrue(key_at in matches)
        self.assertTrue(key_absent in matches)

    def test_match_prefix_4(self):
        trie = Trie()
        key_at = 'at'
        key_absent = 'absent'
        data_at = '@'
        data_absent = ''
        trie.insert( key_at, data_at )
        trie.insert( key_absent, data_absent )

        matches = trie.match_prefix('a')
        self.assertEqual(len(matches), 2)
        self.assertTrue(key_at in matches)
        self.assertTrue(key_absent in matches)


if __name__ == '__main__':
    unittest.main()
