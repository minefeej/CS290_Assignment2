# Course: CS261 - Data Structures
# Student Name: Joseph Minefee
# Assignment: Assignment 2
# Description: Implement a Bag ADT
# Last revised: 1/31/21

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

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
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag.
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes one element from the bag that matches the provided value object and returns true if an item was removed
        or false if otherwise.
        """
        # Loops through the indices of the underlying dynamic array.
        end = self.size()
        for ind in range(end):
            # If the value is found, the value is removed from the dynamic array and True is returned.
            if self.da[ind] == value:
                self.da.remove_at_index(ind)
                return True
        # Else false is returned.
        return False

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the bag that match the provided value object
        """
        # Initializes count to zero.
        count = 0
        # Loops through the indices of the dynamic array and if the value is found, the count increments.
        end = self.size()
        for ind in range(end):
            if self.da[ind] == value:
                count += 1
        # Count is returned.
        return count

    def clear(self) -> None:
        """
        Clears the content of the bag.
        """
        # Creates a new, empty bag and assigns self.da to the new, empty bag.
        new_bag = Bag()
        self.da = new_bag.da

    def equal(self, second_bag: object) -> bool:
        """
        Compares the content of the bag with the content of a second bag and returns True if the bags are equal. Else,
        it returns False.
        """
        # Initialize bag sizes, two empty bags for cloning original bags, and result to False.
        bag_1_size = self.size()
        bag_2_size = second_bag.size()
        clone_1 = Bag()
        clone_2 = Bag()
        result = False

        # Clone bags to clone_1 and clone_2.
        for ind in range(bag_1_size):
            clone_1.add(self.da[ind])
        for ind in range(bag_2_size):
            clone_2.add(second_bag.da[ind])

        # Sort cloned bags.
        clone_1.da.sort()
        clone_2.da.sort()

        # Check if bags are empty.
        if bag_1_size == 0 and bag_2_size == 0:
            result = True

        if bag_1_size == bag_2_size and bag_1_size != 0 and bag_2_size != 0:
            # Loop through the cloned bags and compare the elements.
            for ind in range(bag_1_size):
                if clone_1.da[ind] == clone_2.da[ind]:
                    result = True
                else:
                    result = False

        # Returns the result.
        return result


# BASIC TESTING
if __name__ == "__main__":

    print("\n# size example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)
    print(bag.size())

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
