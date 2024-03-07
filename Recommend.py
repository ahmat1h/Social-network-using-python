# The second class:Recommand which is a subclass of the parent class:Open File
# Used to create the common firends count and also to reccomend friends
# Attributes:filename(str),id(int)
# Behaviour: common_friends(),recommandation_of_friends()
# Decorator: @property
from OpenFile import OpenFile


class Recommand(OpenFile):
    def __init__(self, filename, id):  # initialising all the instances of the class
        super().__init__(filename)   # inheritance using super().__init__ from the parent class OpenFile
        self.member = id
# for the code below I got help from the student Leonardo Koxhaj with the ID:001270098 the part that he helped me is how
    # to do the iterations to get the values into the dictionary and the list

    @property  # I used @property to replace () after the functions so its easier to code and also looks better
# This method is used to create a matrix that will do the common friends count
    def common_friends(self):
        cf_list = []   # cf->common friends. The list that is used to build the count for the common friends
        cf_dictionary = {}     # dictionary that creates the count
        for var in range(len(self.add_info_to_list())):     # Loop to create the count
            cf_list.append([0] * self.read_first_number())   # self.read_first_number() is the number of all the members
    # in the network and in the [0]is the value of the members that are in the social network so it gives the info how
        # many lines should be created for the matrix
        for var in range(len(self.add_info_to_list())):    # loop to count every member and to build the common
            # friens structure
            for var2 in range(len(self.add_info_to_list()[var][1])):   # the loop that will get the size of the
                # values in member
                for key in range(len(self.add_info_to_list())):    # this loop will take the value and repeat it
                    # for all for the size of all members in the network
                    if self.add_info_to_list()[var][1][var2] in self.add_info_to_list()[key][1]:  # comment below
                        # condition if the values in keys
                        cf_list[var][key] += 1     # if this is true it will update the list by adding 1
                    else:
                        cf_list[var][key] += 0    # it will update the list by adding 0
        for var in range(len(self.add_info_to_list())):
            cf_dictionary[self.add_info_to_list()[var][0]] = cf_list[var]  # now we add the values of the list into
            # the dictionary
        return cf_dictionary
# This method removes the members that are friends with the user that we input in the main and then it does
    # recommend what's left /it says who to recommend(who is not already a friend)

    def recommandation_of_friends(self):
        try:   # it is used to avoid the error raised
            select_list = []   # we will need this list and the dicctionary for the iterations below
            recommend_dictionary = {}
            friend_recommend = {}
            select_list.append(self.common_friends[self.member])  # firstly we create the list which does append the
# values that we got from the common friends method
            for var in range(len(self.add_info_to_list())):  # loop to create the dictionary with key members and values
                recommend_dictionary[self.add_info_to_list()[var][0]] = select_list[0][var]  # inheritance used yet
# again from the OpenFile class
            network = dict(self.add_info_to_list())   # here we add the keys that we got from add_info_to_list method
            for key, value in recommend_dictionary.items():   # iteration to ignore the below conditions
                if key == self.member:  # condition to ignore the member_id
                    pass

                elif key in network[self.member]:  # this codition will make sure that the friends of the member do
                    # not display
                    pass
                elif value != 0:   # in here it will ignore the 0 so the ones that they don't have in common
                    friend_recommend[key] = value   # here will be the friend recommend
            no_friends = bool(friend_recommend)  # this will make sure that if a member has no friends to
# recommend it won't recommend any
            if no_friends == False:
                print(f"The friend recommended for member {self.member} is none")  # this is the print for the member
                # that has no friends to recommend
            else:
                highest_common_friends = max(friend_recommend, key=friend_recommend.get)  # the person with the highest
# common friends is the other condition from the one with no friends
                print(f"The friend recommended for member {self.member} is {highest_common_friends}")
        except KeyError:
            print('Member does not exist,please enter a correct member ID')
