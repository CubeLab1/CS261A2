# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from dynamic_array import *

class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Add a new element to the bag.
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Remove one occurrence of the specified value from the bag.
        Return True if an element was removed, False otherwise.
        """
        for i in range(self._da.length()):
            if self._da[i] == value:
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Count the number of occurrences of the specified value in the bag.
        """
        count = 0
        for i in range(self._da.length()):
            if self._da[i] == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clear all elements from the bag.
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        Check if two bags are equal (contain the same elements in the same frequency).
        """
        if self.size() != second_bag.size():
            return False
        first_bag_dict = {}
        second_bag_dict = {}
        for i in range(self._da.length()):
            value = self._da[i]
            if value in first_bag_dict:
                first_bag_dict[value] += 1
            else:
                first_bag_dict[value] = 1
        for i in range(second_bag.size()):
            value = second_bag._da[i]
            if value in second_bag_dict:
                second_bag_dict[value] += 1
            else:
                second_bag_dict[value] = 1
        return first_bag_dict == second_bag_dict

    def __iter__(self):
        """
        Create an iterator for the bag.
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain the next value and advance the iterator.
        """
        if self._index < self._da.length():
            value = self._da[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
