class Node:
    def __init__(self, value=0):
        self.data = value
        self.next = None


class SinglyList:
    def __init__(self):
        self.head = None

    # time complexity - O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # time complexity - O(n)
    def add_last(self, value):
        new_node = Node(value)

        # special case: if list is empty
        if self.head is None:
            self.head = new_node  # newNode itself is first node of list
        else:  # general case: if list already have few nodes
            # traverse till last node
            traverse = self.head
            while traverse.next is not None:
                traverse = traverse.next
            # add address of newNode into last node's next
            traverse.next = new_node

    # time complexity - O(n)
    def display(self):
        print("List: ", end='')
        traverse = self.head
        while traverse is not None:
            print(traverse.data, end=", ")
            traverse = traverse.next
        print()

    # time complexity - O(n)
    def add_at_pos(self, val, pos):
        # spl 4. invalid pos( < 1)
        if pos < 1:
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
                if traverse is None:
                    raise Exception("Invalid position " + str(pos))
            # add node at that pos
            new_node.next = traverse.next
            traverse.next = new_node

    # time complexity - O(1)
    def del_first(self):
        if self.head is None:
            raise Exception("List is empty.")
        self.head = self.head.next

    # time complexity - O(n) or O(pos)
    def del_at_pos(self, pos):
        # spl 3: if pos < 1, throw exception
        if pos < 1:
            raise Exception("Invalid position " + str(pos))
        # spl 1: list is empty & 2: pos == 1
        if self.head is None or pos == 1:
            self.del_first()
        else:
            traverse = self.head
            for i in range(1, pos-1):
                traverse = traverse.next
                # spl 4: if pos > length, throw exception
                if traverse is None:
                    raise Exception("Invalid position " + str(pos))
            temp = traverse.next
            # spl 5: pos == length, if temp is null, throw exception
            if temp is None:
                raise Exception("Invalid position " + str(pos))
            traverse.next = temp.next

    # time complexity - O(n)
    def del_all(self):
        while self.head is not None:
            self.del_first()
        # head = null;

    # time complexity - O(n)
    def del_last(self):
        # spl1: list is empty, spl2: list have only one node.
        if self.head is None or self.head.next is None:
            self.del_first()
        else:
            temp = None
            traverse = self.head
            while traverse.next is not None:
                temp = traverse
                traverse = traverse.next
            temp.next = None


def main():
    list1 = SinglyList()
    list1.add_last(10)
    list1.add_last(20)
    list1.add_last(30)
    list1.add_first(40)
    list1.display()
    list1.add_at_pos(50, 2)
    list1.display()
    list1.del_first()
    list1.display()
    list1.del_last()
    list1.display()
    list1.del_at_pos(3)
    list1.display()


if __name__ == "__main__":
    main()
