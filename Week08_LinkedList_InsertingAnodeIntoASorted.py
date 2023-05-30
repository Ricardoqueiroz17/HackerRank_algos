class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


def sortedInsert(llist, data):
    # Write your code here

    node = Node(data)
    if llist is None:
        return node

    if node.data <= llist.data:
        node.next = llist
        return node

    current = llist.next
    previous = llist
    while current is not None:
        if node.data <= current.data:
            break
        previous = current
        current = current.next

    previous.next = node
    if current is not None:
        node.next = current
        node.previous = previous

    return llist