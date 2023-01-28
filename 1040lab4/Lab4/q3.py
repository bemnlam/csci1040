class Node(object):
    def __init__(self, v, n):
        self.value = v
        self.next = n

class LinkedList(object):
    def __init__(self):
        self.firstLink = None
    def add (self, newElement):
        self.firstLink = Node( newElement, self.firstLink)
    def test (self, testValue): # see if test value is in link list
        pass
    def remove( self, testValue): # remove value from linked list
        pass
    def len (self): # return size of linked list
        pass
