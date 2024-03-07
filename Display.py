# The third class is:Display which is inherited from the parent class:OpenFile
# It is used to print the least friend and print how many friends a member has
# Attributes: filename(str),ID(int)
# Behaviour: display_nr_of_friends()
from OpenFile import OpenFile


class Display(OpenFile):  # declaring the instances
    def __init__(self, filename, id):
        super().__init__(filename)  # inheritance from the parent class(OpenFile)
        self.member = id
# This method is used to display the number of friends(feature 3i)

    def display_nr_of_friends(self):
        network = self.convert()  # this list is used to find the number of friends entered
        for key, value in network.items():  # loop to count the number of friends
            if key == self.member:
                number_of_friends = len(value)  # there is the count which will count the length of the values if the
# key is equal to the one that will be given in the input
                print(f'The member {self.member} has {number_of_friends}friends')   # this print will display the
# number of friends