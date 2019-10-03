#Node class.
class Node:

    #initialize any node instance.
    def __init__(self, data):
        self.data = data #data is given for each object of a node.
        self.next = None # initializing the next of any node to null at first.

#linked_list class.
class LinkedList:
    def __init__(self):
        # creating an empty linked list that it's head pointing to no nodes at first.
        self.head = None

    # function to print any linked list object.
    def printList(self):
        # take first node in the llist object and print it's data then keep printing the next data till u have no data.
        temp = self.head
        while (temp):# temp not null.
            print(temp.data)
            temp = temp.next

#Creating a linked list with 4 nodes.
#create an object of a linked list.
llist = LinkedList()

# Assigning the head to point to the first node object containing data of "1".
llist.head = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
# All the previous nodes has it's data but it's next(pointer to next node) is set to null for now.
# let's link em all up together.
llist.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = None

llist.printList()
