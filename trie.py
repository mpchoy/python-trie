class Node:
    """A Trie node"""
    def __init__( self, key ):
        self.key = key # TODO remove
        self.children = {}
        self.data = None

    def __str__( self ):
        print "<" + self.key + ">"


class Trie:
    """
    A simple trie structure
    Keys must be orderable.
    """
    def __init__( self ):
        self.root = Node( '' )

    def insert( self, key, data ):
        node = self.root
        i = 0
        for k in key:
            if k not in node.children:
                node.children[k] = Node( k )
            node = node.children[k]
        node.data = data

    def get( self, key ):
        node = self.root

        for k in key:
            if k not in node.children:
                return None
            node = node.children[k]

        return node.data
