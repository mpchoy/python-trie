class Node:
    """A Trie node"""
    def __init__( self ):
        self.children = {}
        self.data = None

    def has_data( self ):
        return self.data is not None


class Trie:
    """
    A simple trie structure
    Keys must be orderable.
    Data cannot be None.
    """
    def __init__( self ):
        self.root = Node()

    def insert( self, key, data=0 ):
        """Insert the key with the given data"""
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
        """Removes the key. Also removes orphan nodes.
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
            else:
                break # stop pruning
        return data

    def match_prefix( self, prefix ):
        """Find all strings that match given prefix.
        If prefix itself is in the trie, will include it in the results.
        Returns:
        A list of words matching the prefix.
        """
        prefix_root = self._get_node( prefix )

        if prefix_root is None:
            return []

        matches = []
        self._match_prefix_r( prefix_root, matches, prefix )

        return matches

    def _match_prefix_r( self, node, matches, match ):
        if node.has_data():
            matches.append( match )
        for k, child in node.children.iteritems():
            self._match_prefix_r( child, matches, match+k )
        return


if __name__ == '__main__':
    trie = Trie()
    f = open('trie.dict', 'r')

    for line in f:
        tokens = [ x.strip() for x in line.split(':') ]
        trie.insert( tokens[0], tokens[1] )

    f.close()

    while True:
        search_for = raw_input("Please search a word or type exit: ")
        search_for = search_for.strip()

        if search_for == "exit":
            break

        data = trie.get(search_for)
        if data is not None:
            print "The data is: " + str(data)
        else:
            print "Sorry, your word was not found."

        matches = trie.match_prefix( search_for )
        matches.remove( search_for )
        if matches:
            print "Some prefix matches:" + str(matches)
