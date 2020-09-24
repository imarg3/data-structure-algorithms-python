class Stack:
    def __init__(self):
        self.arr = list()

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[len(self.arr) - 1]

    def is_empty(self):
        return len(self.arr) == 0


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.visited = False

    def to_string(self):
        return "Node [data=" + str(self.data) + "]"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            traverse = self.root
            while True:
                if val < traverse.data:
                    if traverse.left is None:
                        traverse.left = new_node
                        break
                    else:
                        traverse = traverse.left
                else:  # if(val >= traverse.data)
                    if traverse.right is None:
                        traverse.right = new_node
                        break
                    else:
                        traverse = traverse.right

    def recur_add(self, traverse, val):
        if val < traverse.data:
            if traverse.left is None:
                traverse.left = Node(val)
            else:
                self.recur_add(traverse.left, val)
        else:
            if traverse.right is None:
                traverse.right = Node(val)
            else:
                self.recur_add(traverse.right, val)

    def recursion_add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.recur_add(self.root, val)

    def recur_pre_order(self, traverse):
        if traverse is None:
            return
        print(str(traverse.data) + ", ", end='')
        self.recur_pre_order(traverse.left)
        self.recur_pre_order(traverse.right)

    def recursion_pre_order(self):
        print("Pre: ", end='')
        self.recur_pre_order(self.root)
        print()

    def recur_in_order(self, traverse):
        if traverse is None:
            return
        self.recur_in_order(traverse.left)
        print(str(traverse.data) + ", ", end='')
        self.recur_in_order(traverse.right)

    def recursion_in_order(self):
        print("In : ", end='')
        self.recur_in_order(self.root)
        print()

    def recur_post_order(self, traverse):
        if traverse is None:
            return
        self.recur_post_order(traverse.left)
        self.recur_post_order(traverse.right)
        print(str(traverse.data) + ", ", end='')

    def recursion_post_order(self):
        print("Post:", end='')
        self.recur_post_order(self.root)
        print()

    def recur_delete_order(self, traverse):
        if traverse is None:
            return
        self.recur_delete_order(traverse.left)
        traverse.left = None
        self.recur_delete_order(traverse.right)
        traverse.right = None
        # traverse = None

    def recursion_delete_order(self):
        self.recur_delete_order(self.root)
        self.root = None

    def recur_height(self, traverse):
        if traverse is None:
            return -1
        hl = self.recur_height(traverse.left)
        hr = self.recur_height(traverse.right)
        return max(hl, hr) + 1

    def recursion_height(self):
        return self.recur_height(self.root)

    def recur_find(self, traverse, val):
        if traverse is None:
            return None
        if val == traverse.data:
            return traverse
        if val < traverse.data:
            return self.recur_find(traverse.left, val)
        else:
            return self.recur_find(traverse.right, val)

    def recursion_find(self, val):
        return self.recur_find(self.root, val)

    def find(self, val):
        traverse = self.root
        while traverse is not None:
            if val == traverse.data:
                return traverse
            if val < traverse.data:
                traverse = traverse.left
            else:  # if(val < traverse.data)
                traverse = traverse.right
        return None

    def pre_order(self):
        s = Stack()
        # 1. start traversing from self.root
        traverse = self.root
        print("PRE : ", end='')
        while traverse is not None or not s.is_empty():
            while traverse is not None:
                # 2. visit traverse
                print(traverse.data, end=", ")
                # 3. if traverse has right, push traverse.right on stack
                if traverse.right is not None:
                    s.push(traverse.right)
                # 4. go to left of traverse
                traverse = traverse.left
            # 5. repeat 2-5 until traverse is None
            if not s.is_empty():
                traverse = s.pop()  # 6. pop Node from stack into traverse
        # 7. repeat 2-6, until traverse is None or stack is isEmpty
        print()

    def in_order(self):
        s = Stack()
        traverse = self.root
        print("IN  : ", end='')
        while traverse is not None or not s.is_empty():
            while traverse is not None:
                s.push(traverse)
                traverse = traverse.left
            if not s.is_empty():
                traverse = s.pop()
                print(traverse.data, end=", ")
                traverse = traverse.right
        print()

    def post_order(self):
        s = Stack()
        # start traverse from self.root
        traverse = self.root
        print("POST: ", end='')
        # while traverse is not None or stack is not isEmpty
        while traverse is not None or not s.is_empty():
            # until None is reached
            while traverse is not None:
                # push traverse on stack
                s.push(traverse)
                # go to traverse's left
                traverse = traverse.left
            # if stack is not isEmpty
            if not s.is_empty():
                # pop Node from stack into traverse
                traverse = s.pop()
                # if traverse's right is present & visited
                if traverse.right is None or traverse.right.visited is True:
                    # visit traverse & mark it as visited
                    print(traverse.data, end=", ")
                    traverse.visited = True
                    # make traverse None (so that next Node will be popped from stack)
                    traverse = None
                # otherwise
                else:
                    # push Node on stack
                    s.push(traverse)
                    # go to its right
                    traverse = traverse.right
        print()


def main():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(30)
    bst.add(10)
    bst.add(90)
    bst.add(100)
    bst.add(40)
    bst.add(70)
    bst.add(80)
    bst.add(20)
    bst.add(60)
    bst.recursion_delete_order()

    bst.recursion_add(50)
    bst.recursion_add(30)
    bst.recursion_add(10)
    bst.recursion_add(90)
    bst.recursion_add(100)
    bst.recursion_add(40)
    bst.recursion_add(70)
    bst.recursion_add(80)
    bst.recursion_add(20)
    bst.recursion_add(60)

    bst.recursion_pre_order()
    bst.pre_order()
    bst.recursion_in_order()
    bst.in_order()
    bst.recursion_post_order()
    bst.post_order()

    print("Height: " + str(bst.recursion_height()))

    temp = bst.recursion_find(75)
    # temp = bst.find(80)
    if temp is None:
        print("Node not found.")
    else:
        print("Node found: " + temp.toString())

    bst.recursion_delete_order()
    print("Height: " + str(bst.recursion_height()))


if __name__ == "__main__":
    main()
