from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        # Initializes a CompactString object representing the string given in orig_str
        self.data = DoublyLinkedList()
        if orig_str != '':
            count = 1
            curr_elem = orig_str[0]
            for elem in orig_str:
                if elem == curr_elem:
                    count += 1
                else:
                    self.data.add_last((curr_elem, count))
                    count = 1
                    curr_elem = elem
            self.data.add_last((curr_elem, count))

    def __add__(self, other):
        # Creates and returns a CompactString object that represent
        # the concatenation of self and other, also of type CompactString
        concatenated = CompactString('')

        node = self.data.header.next
        while node.data is not None:
            concatenated.data.add_last(node.data)
            node = node.next

        node = node.prev
        other_node = other.data.header.next

        if node.data[0] == other_node.data[0]:
            concatenated.data.delete_last()
            count = node.data[1] + other_node.data[1]
            concatenated.data.add_last((node.data[0], count))
            other_node = other_node.next

        while other_node.data is not None:
            concatenated.data.add_last(other_node.data)
            other_node = other_node.next

        return concatenated

    def __lt__(self, other):
        # returns True if”f self is lexicographically less than other,
        # also of type CompactString
        self_node = self.data.header.next
        other_node = other.data.header.next

        if self_node.data is None and other_node.data is None:
            return False
        elif self_node.data is None and other_node.data is not None:
            return True
        elif self_node.data is not None and other_node.data is None:
            return False
        else:
            while (self_node.data is not None) and (other_node.data is not None):
                if self_node.data[0] < other_node.data[0]:
                    return True
                elif self_node.data[0] > other_node.data[0]:
                    return False
                else:
                    if self_node.next.data is None and self_node.next.data is None:
                        if self_node.data[1] < other_node.data[1]:
                            return True
                        else:
                            return False
                    elif self_node.next.data is None and other_node.next.data is not None:
                        return True
                    elif self_node.next.data is not None and other_node.next.data is None:
                        return False
                    elif self_node.data[1] < other_node.data[1]:
                        return False
                    elif self_node.data[1] > other_node.data[1]:
                        return True
                    else:
                        self_node = self_node.next
                        other_node = other_node.next
        return True

    def __le__(self, other):
        # returns True if”f self is lexicographically less than or equal to other,
        # also of type CompactString
        self_node = self.data.header.next
        other_node = other.data.header.next

        if self_node.data is None and other_node.data is None:
            return True
        elif self_node.data is None and other_node.data is not None:
            return True
        elif self_node.data is not None and other_node.data is None:
            return False
        else:
            while (self_node.data is not None) and (other_node.data is not None):
                if self_node.data[0] < other_node.data[0]:
                    return True
                elif self_node.data[0] > other_node.data[0]:
                    return False
                else:
                    if self_node.next.data is None and self_node.next.data is None:
                        if self_node.data[1] <= other_node.data[1]:
                            return True
                        else:
                            return False
                    elif self_node.next.data is None and other_node.next.data is not None:
                        return True
                    elif self_node.next.data is not None and other_node.next.data is None:
                        return False
                    elif self_node.data[1] < other_node.data[1]:
                        return False
                    elif self_node.data[1] > other_node.data[1]:
                        return True
                    else:
                        self_node = self_node.next
                        other_node = other_node.next
        return True

    def __gt__(self, other):
        # returns True if”f self is lexicographically greater than other,
        # also of type CompactString
        self_node = self.data.header.next
        other_node = other.data.header.next

        if self_node.data is None and other_node.data is None:
            return False
        elif self_node.data is None and other_node.data is not None:
            return False
        elif self_node.data is not None and other_node.data is None:
            return True
        else:
            while (self_node.data is not None) and (other_node.data is not None):
                if self_node.data[0] < other_node.data[0]:
                    return False
                elif self_node.data[0] > other_node.data[0]:
                    return True
                else:
                    if self_node.next.data is None and self_node.next.data is None:
                        if self_node.data[1] > other_node.data[1]:
                            return True
                        else:
                            return False
                    elif self_node.next.data is None and other_node.next.data is not None:
                        return False
                    elif self_node.next.data is not None and other_node.next.data is None:
                        return True
                    elif self_node.data[1] < other_node.data[1]:
                        return True
                    elif self_node.data[1] > other_node.data[1]:
                        return False
                    else:
                        self_node = self_node.next
                        other_node = other_node.next
        return True

    def __ge__(self, other):
        # returns True if”f self is lexicographically greater than or equal to other,
        # also of type CompactString
        self_node = self.data.header.next
        other_node = other.data.header.next

        if self_node.data is None and other_node.data is None:
            return True
        elif self_node.data is None and other_node.data is not None:
            return False
        elif self_node.data is not None and other_node.data is None:
            return True
        else:
            while (self_node.data is not None) and (other_node.data is not None):
                if self_node.data[0] < other_node.data[0]:
                    return False
                elif self_node.data[0] > other_node.data[0]:
                    return True
                else:
                    if self_node.next.data is None and self_node.next.data is None:
                        if self_node.data[1] >= other_node.data[1]:
                            return True
                        else:
                            return False
                    elif self_node.next.data is None and other_node.next.data is not None:
                        return False
                    elif self_node.next.data is not None and other_node.next.data is None:
                        return True
                    elif self_node.data[1] < other_node.data[1]:
                        return True
                    elif self_node.data[1] > other_node.data[1]:
                        return False
                    else:
                        self_node = self_node.next
                        other_node = other_node.next
        return True

    def __repr__(self):
        # Creates and returns the string representation (of type str) of self
        return "".join([str(elem[0] * elem[1]) for elem in self.data])
