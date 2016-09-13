from .node import Node


class UnOrderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.value == item:
                found = True
                break
            current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.value == item:
                found = True
                break
            previous = current
            current = current.get_next()

        if previous:
            previous.set_next(current.get_next())
        else:
            self.head = current.get_next()

    @property
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

def main():
    new_list = UnOrderedList()
    new_list.add(5)
    new_list.add(7)
    new_list.add(3)
    new_list.add(8)
    print new_list.size
    print new_list.search(10)
    new_list.remove(8)
    new_list.remove(7)
    print new_list.size

if __name__=='__main__':
    main()
