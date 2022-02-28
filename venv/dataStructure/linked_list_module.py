class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = node

    def print_list(self):
        list_content = ''
        temp = self.head
        while temp is not None:
            list_content = list_content + "-->" + temp.data
            temp = temp.next
        list_content=list_content[3:]
        print("Linked List : {}".format(list_content))

    def prepend(self,data):
        node = Node(data)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def insert_after_node(self,data,prev_node_data):
        node = Node(data)
        temp=self.head
        prev_node=None
        while temp is not None:
            if temp.data == prev_node_data:
                prev_node=temp
                break
            temp = temp.next
        if prev_node is not None:
            node.next=prev_node.next
            prev_node.next=node

if __name__ == '__main__':
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.print_list()
    llist.insert_after_node("M", "C")
    llist.print_list()
    llist.prepend("K")
    llist.print_list()
