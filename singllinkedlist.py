class Node:
    ''' class for creating node  '''

    def __init__(self, value):
        self.value = value
        self.next = None


class linked_list:
    ''' class for creating linked list '''

    def __init__(self, head=None):
        self.head = head

    def push_front(self, new_node):
        ''' pushing the new element to be the node'''
        current = self.head
        if self.head:
            self.head = new_node
            self.head.next = current

        else:
            self.head = new_node

    @property
    def top_front(self):
        '''  method for getting head '''
        if self.head:
            return self.head
        return None

    @property
    def pop_front(self):
        ''' method for poping head '''
        try:
            current = self.head
            self.head = current.next
            return current
        except:
            return None

    def push_pack(self, new_node):
        ''' method for push element to pack '''
        current = self.head
        try:
            while (current.next != None):
                current = current.next
            current.next = new_node
        except:
            return None

    @property
    def top_pack(self):
        ''' property for getting the last element '''
        current = self.head
        try:
            while(current.next != None):
                current = current.next
            return current.value
        except:
            return None

    @property
    def pop_pack(self):
        ''' property for poping the last element '''
        try:
            tail = self.top_pack
            self.delete(tail.value)
            return tail.value
        except:
            return None

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def delete(self, value):
        current = self.head
        prev = None
        while current.value != value and current.next:
            prev = current
            current = current.next
        if current.value == value:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

    def get_postion(self, postion):
        counter = 0
        current = self.head

        if postion >= 0:
            while counter != postion and current:
                current = current.next
                counter += 1
            if counter == postion:
                return current
            return None
        return None

    def insert(self, element, postion):
        prev = None
        try:
            current_element = self.get_postion(postion)
        except:
            return None
        current = self.head
        while current and current.value != current_element.value:
            prev = current
            current = current.next

        if current:
            if prev:
                prev.next = element
                element.next = current_element
            else:
                self.head = element
