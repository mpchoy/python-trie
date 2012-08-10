class Node:
    """A Trie node"""
    def __init__( self, key ):
        self.key = key
        self.children = []

    def __str__( self ):
        print "<" + self.key + ">"


class Trie:
    """A simple trie structure"""
    def __init__( self ):
        self.root = None
