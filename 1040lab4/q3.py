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
        ptr = self.firstLink
        while ptr!=None:
            if ptr.value == testValue:
                return True
            else:
                ptr = ptr.next
        return False

    def remove( self, testValue): # remove value from linked list
        # check if empty LL
        if self.firstLink == None:
            return
        
        ptr = self.firstLink
        nptr = None
        
        # check if first is suitable value
        if ptr.value == testValue:
            print '> match'
            self.firstLink = ptr.next
            return

        # if not the first node
        if ptr.next == None:
            pass
        else:
            nptr = ptr.next

        while nptr != None:
            #print "curr: " + str(ptr.value) + "\tnext: " + str(nptr.value)
            if nptr.value == testValue:
                ptr.next = nptr.next
                nptr.next = None
                return
            ptr = nptr
            nptr = nptr.next

        return

    def len (self): # return size of linked list
        ptr = self.firstLink
        cnt = 0
        #lst = list()
        while ptr!=None:
        #    lst.append(ptr.value)
            ptr = ptr.next
            cnt +=1
        #print lst
        return cnt


# LL = LinkedList()
# print LL.len()
# LL.add(20)
# LL.add(30)
# LL.add(40)
# LL.add(50)

# print LL.len()
# print LL.test(30)
# print LL.test(3)
# LL.remove(20)
# LL.remove(40)
# LL.remove(50)
# LL.remove(30)
# LL.remove(0)
# print LL.len()
# print LL.test(30)

