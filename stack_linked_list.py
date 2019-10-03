# Node class.
class StackNode:
    def __init__(self, data):
        # data in the node.
        self.data = data

        # the next node my current node is pointing towards.
        self.next = None

# Stack class.


class Stack:  # should contain(is_empty(), push(), pop(), peek()).
    def __init__(self):
        # at first the stack is empty.
        self.base = None

    # check if the stack is empty.
    def is_empty(self):
        if not self.base:
            return True
        else:
            return False

    def push(self, data):
        # create a node with the given pushed data.
        pushed_node = StackNode(data)
        # point to the next element in the stack after the pushed node.
        pushed_node.next = self.base
        # make the pushed node the base of the sub_stack of my big stack.
        self.base = pushed_node
        print("pushed " + str(pushed_node.data) + " to the stack.\n")

    def pop(self):
        if self.is_empty():
            print("The stack is empty.")
        # pop the last element that has been pushed into the stack.
        popped_node = self.base
        self.base = self.base.next
        pop_node = popped_node.data
        print("popped " + str(pop_node) + " from the stack.\n")

    #look at the top element in the stack.
    def peek(self):
        if self.is_empty():
            print("There is no element in the stack to look at.")
        # return the data of the last node that has been pushed.
        print(str(self.base.data) + "\n")

    def print_stack(self):
        # top node in the stack.
        top_node = self.base
        while(top_node): # loop till there is no top node in the sub_stacks of my stack.
            print(top_node.data)
            top_node = top_node.next






stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.pop()
stack.peek()

stack.print_stack()


