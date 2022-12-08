from DoublyLinkedList import DoublyLinkedList


class Integer:

    def __init__(self, num_str):
        # Initializes an Integer object representing the value given in the string num_str
        self.data = DoublyLinkedList()

        if num_str != '':
            for num in num_str:
                self.data.add_last(int(num))

    def __add__(self, other):
        # Creates and returns an Integer object that represent the sum of self and other, also of type Integer
        total = Integer('')

        if len(self.data) < len(other.data):
            long = other.data
            short = self.data
        else:
            long = self.data
            short = other.data

        carry = 0
        short_val = short.trailer.prev
        long_val = long.trailer.prev

        while short_val.data is not None:
            added = short_val.data + long_val.data
            if added > 9 and carry == 0:
                carry = 1
                added = added - 10
                total.data.add_first(added)
            elif added > 9 and carry == 1:
                added = added - 10
                total.data.add_first(added + 1)
                carry = 1
            else:
                total.data.add_first(added)
            short_val = short_val.prev
            long_val = long_val.prev

        while long_val.data is not None:
            if carry == 0:
                total.data.add_first(long_val.data)
            else:
                if long_val.data + carry < 9:
                    total.data.add_first(long_val.data + carry)
                    carry = 0
                else:
                    diff = (long_val.data + carry) - 10
                    total.data.add_first(diff)
                    carry = 1
            long_val = long_val.prev

        if (short_val.data is None and long_val.data is None) and carry != 0:
            total.data.add_first(carry)

        if total.data.header.next.data == 0:
            total.data.delete_first()

        return total

    def __repr__(self):
        # Creates and returns the string representation of self
        return "".join([str(elem) for elem in self.data])

    def __mul__(self, other):
        # Creates and returns an Integer object that represent
        # the multiplication of self and other, also of type Integer
        product = Integer('0')

        if len(self.data) < len(other.data):
            long = other.data
            short = self.data
        else:
            long = self.data
            short = other.data

        if (short.header.next.data == 0 and short.size == 1) or (long.header.next.data == 0 and long.size == 1):
            return product

        count = 0
        short_val = short.trailer.prev

        while short_val is not short.header:
            long_val = long.trailer.prev
            string = ''
            carry = 0
            while long_val is not long.header:
                total = carry + (long_val.data * short_val.data)
                if long_val is not long.header.next:
                    carry = total // 10
                    string = (str(total % 10)) + string
                else:
                    string = str(total) + string
                long_val = long_val.prev
            string = string + ('0' * count)
            product = product + Integer(string)
            count += 1
            short_val = short_val.prev

        return product
