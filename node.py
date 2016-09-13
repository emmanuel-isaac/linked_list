class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    @staticmethod
    def print_nodes(node):
        while node:
            print node
            node = node.get_next()

    def __str__(self):
        return "{}".format(self.value)


def main():
    a = Node(3)
    b = Node(5)
    c = Node(7)

    a.set_next(b)
    b.set_next(c)

    Node.print_nodes(a)

if __name__=='__main__':
    main()
