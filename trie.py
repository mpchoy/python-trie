class Node:
    """A Trie node"""
    def __init__( self ):
        self.children = {}
        self.data = None

    def __str__( self ):
        print "<" + self.data + ">"


class Trie:
    """
    A simple trie structure
    Keys must be orderable.
    """
    def __init__( self ):
        self.root = Node()

    def insert( self, key, data ):
        node = self.root
        i = 0
        for k in key:
            if k not in node.children:
                node.children[k] = Node()
            node = node.children[k]
        node.data = data

    def get( self, key ):
        """Retrieve the data referenced by the key.
        Returns:
        The key's data, if it exists. Else, return None.
        """
        node = self._get_node(key)
        return node.data if node else None

    def _get_node( self, key ):
        node = self.root

        for k in key:
            if k not in node.children:
                return None
            node = node.children[k]
        return node

    def remove( self, key ):
        """Removes the key.
        Also removes orphan nodes.
        Returns:
        The key's data, if it exists. Else, return None.
        """
        node = self.root
        trail = []

        for k in key:
            if k not in node.children:
                return None

            trail.append( node )
            node = node.children[k]

        data = node.data
        node.data = None
        while trail:
            prev = trail.pop()
            k = key[len(trail)]
            if not prev.children[k].children:
                del prev.children[k]
        return data

    def match_prefix( self, prefix ):
        prefix_root = self._get_node( prefix )

        if prefix_root is None:
            return []

        matches = []
        self._match_prefix_r( prefix_root, matches, prefix )

        matches.remove(prefix)
        return matches

    def _match_prefix_r( self, node, matches, match ):
        for key, child in node.children.iteritems():
            self._match_prefix_r( child, matches, match+key )
        if node.data is not None:
            matches.append( match )
        return
