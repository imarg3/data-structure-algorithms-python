class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None


class SinglyCircularList:

    def __init__(self):
        self.head = None
        self.count = 0

    # time complexity - O(1)
    def add_first(self, val):
        # create new node
        new_node = Node(val)
        # spl: list is empty
        if self.head is None:
            # add node at the start of list
            self.head = new_node
            # make it circular
            new_node.next = self.head
        else:
            # traverse till last node
            traverse = self.head
            while traverse.next != self.head:
                traverse = traverse.next
            # new_node's next to head
            new_node.next = self.head
            # last node's next to new node
            traverse.next = new_node
        self.head = new_node
        self.count = self.count + 1

    # time complexity - O(n)
    def add_last(self, val):
        # create new node
        new_node = Node(val)
        # spl: list is empty
        if self.head is None:
            # add node at the start of list
            self.head = new_node
            # make it circular
            new_node.next = self.head
        else:
            # traverse till last node
            traverse = self.head
            while traverse.next != self.head:
                traverse = traverse.next
            # new_node's next to head
            new_node.next = self.head
            # last node's next to new node
            traverse.next = new_node
        self.count = self.count + 1

    # time complexity - O(n)
    def display(self):
        print("List: ", end='')
        if self.head is not None:
            traverse = self.head
            while True:
                print(traverse.data, end=", ")
                traverse = traverse.next
                if traverse == self.head:
                    break
        print()

    # time complexity - O(n)
    def add_at_pos(self, val, pos):
        # spl 4. invalid pos ( < 1 or > length)
        if pos < 1 or pos > (self.count + 1):
            raise Exception("Invalid position " + str(pos))
        # spl 1. if list is empty OR spl 2. add at pos = 1
        if self.head is None or pos == 1:
            self.add_first(val)
        else:
            # create a new node
            new_node = Node(val)
            # traverse till pos - 1
            traverse = self.head
            for i in range(1, pos - 1):
                # spl 3. if pos to add is beyond length of list, throw error
                traverse = traverse.next
            # add node at that pos
            new_node.next = traverse.next
            traverse.next = new_node
            self.count = self.count + 1

    # time complexity - O(1)
    def del_first(self):
        # spl1: list is empty
        if self.head is None:
            raise Exception("List is empty.")
        # spl2: list contains only one element
        if self.head == self.head.next:
            self.head = None
        else:
            # traverse till last node
            traverse = self.head
            while traverse.next != self.head:
                traverse = traverse.next
            # take head to the next node (2nd)
            self.head = self.head.next
            # last node's next to the new head
            traverse.next = self.head
        self.count = self.count - 1

    def del_at_pos(self, pos):
        # similar to singly linear linked list
        pass

    # time complexity - O(n)
    def del_all(self):
        # // O(n2)
        # while self.head is not None:
        # 	del_first()

        # // O(n)
        # // if have single node, delete it.
        if self.head is None or self.head.next == self.head:
            self.head = None
        else:
            # convert circular list to linear list
            temp = self.head
            self.head = self.head.next
            temp.next = None
            # // delete all nodes in linear list
            while self.head is not None:
                temp = self.head
                self.head = self.head.next
                temp.next = None


def main():
    l1 = SinglyCircularList()
    l1.add_last(11)
    l1.add_last(22)
    l1.add_last(33)
    l1.add_first(44)
    l1.display()
    l1.add_at_pos(55, 5)
    l1.display()
    l1.del_first()
    l1.display()
    # l1.delLast()
    # l1.display()
    # l1.delAtPos(3)
    # l1.display()


if __name__ == "__main__":
    main()
