class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None
        self.prev = None


class DoublyList:

    def __init__(self):
        self.head = None
        self.count = 0

    # time complexity - O(1)
    def add_first(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count = self.count + 1

    # time complexity - O(n)
    def add_last(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            traverse = self.head
            while traverse.next is not None:
                traverse = traverse.next
            traverse.next = new_node
            new_node.prev = traverse
        self.count = self.count + 1

    # time complexity - O(n)
    def display(self):
        temp = None
        # display forward
        print("Fwd List: ", end='')
        traverse = self.head
        while traverse is not None:
            print(traverse.data, end=", ")
            temp = traverse
            traverse = traverse.next
        print()
        # display reverse
        print("Rev List: ", end='')
        traverse = temp
        while traverse is not None:
            print(traverse.data, end=", ")
            traverse = traverse.prev
        print()

    # time complexity - O(n)
    def add_at_pos(self, val, pos):
        # // spl3: add at last pos
        if pos == self.count + 1:
            self.add_last(val)
        # // spl4: invalid pos
        elif pos < 1 or pos > self.count + 1:
            raise Exception("Invalid position " + str(pos))
        # // spl1: list is empty or spl2: pos is 1
        elif self.head is None or pos == 1:
            self.add_first(val)
        else:
            new_node = Node(val)
            # // traverse till pos-1
            traverse = self.head
            for i in range(1, pos - 1):
                traverse = traverse.next
            # // mark its next node as temp
            temp = traverse.next
            # // add new_node between traverse & temp
            new_node.next = temp
            new_node.prev = traverse
            traverse.next = new_node
            temp.prev = new_node
            self.count = self.count + 1

    # time complexity - O(1)
    def del_first(self):
        # // spl1: list is empty
        if self.head is None:
            raise Exception("List is empty.")
        # // spl2: if list have only one element
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.count = self.count - 1

    def del_at_pos(self, pos):
        # // spl1: list is empty or spl2: pos = 1
        if self.head is None or pos == 1:
            self.del_first()
        else:
            # // spl3: invalid pos
            if pos < 1 or pos > self.count:
                raise Exception("Invalid position " + str(pos))
            # // traverse till pos
            traverse = self.head
            for i in range(1, pos):
                traverse = traverse.next
            # // delete traverse node
            traverse.prev.next = traverse.next
            if traverse.next is not None:  # // spl4: if not last node to delete.
                traverse.next.prev = traverse.prev
            self.count = self.count - 1

    # time complexity - O(n)
    def del_all(self):
        while self.head is not None:
            self.del_first()

    # head = None

    def count_nodes(self):
        cnt = 0
        traverse = self.head
        while traverse is not None:
            cnt = cnt + 1
            traverse = traverse.next
        return cnt


def main():
    l1 = DoublyList()
    l1.add_last(11)
    l1.add_last(22)
    l1.add_last(33)
    l1.add_first(44)
    l1.display()
    l1.add_at_pos(55, 5)
    l1.display()
    l1.del_first()
    l1.display()
    l1.del_at_pos(2)
    l1.display()


if __name__ == "__main__":
    main()
