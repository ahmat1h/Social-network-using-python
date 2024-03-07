# The first and the main class:OpenFile.It is used to open the textfiles and read and split the lines and also to
# create the social network and print the social network
# Attributes:File(str)
# Behaviour:open_file(),read_first_number(),social_network(),convert(),add_info_to_list(),print_social_network()
class OpenFile:
    def __init__(self, file):  # Init is the constructor and self is used for all the instances in the classs
        self.file = file

    # In the method below we first read the lines and splits them with .split() method.Also it does append them
    # in the list created

    def open_file(self):
        try:
            list_people = []  # creating the list to append the lines later
            with open(self.file) as file:
                file.readline()  # read the lines so we can get the members of the social network
                for unit in file:  # loop to split the members and append them into the list
                    split = unit.split()  # split
                    list_people.append(split)  # append
            return list_people
        except FileNotFoundError:  # There can be an error raised so to avoid this we create the try and expect
            return False

    # Created this method to read the first line and it needs to be the same one for all the members
    def read_first_number(self):  # it takes the first number and counts the members
        with open(self.file) as file:  # open the files again
            members = file.readline()[:1]  # describe to read only the first line
        return int(members)

# this method is used to create the social network
    def social_network(self):
        adjacency_list = [[] for _ in range(self.read_first_number())] # firsly I create two lists that will be used in
        # the iterations
        adjacency_list2 = [[] for _ in range(self.read_first_number())]
        for i in range(len(self.open_file())):  # loop
            adjacency_list[int(self.open_file()[i][0])].append(int(self.open_file()[i][1]))  # this will append the from 0 to 1
            adjacency_list2[int(self.open_file()[i][1])].append(int(self.open_file()[i][0])) # this will append from 1 to 0
        total = [0] * self.read_first_number()  # this is created to make the two lists together and now we add the
        # first line[0] which is the number of members to the second line which is the maximum members
        for i in range(self.read_first_number()):
            total[i] = adjacency_list[i] + adjacency_list2[i]  # here the two lists are added together
        return list(total)
# this method converts into a dictionary
    def convert(self):
        dict_social_network = {}  # the dict that we will need
        for i in range(len(self.social_network())):  # loop
            dict_social_network[i] = self.social_network()[i]  # we turn the social network into a dict
        return  dict_social_network

    # Creating this methods to add the keys of the dictionary nw_dictionary into a list
    def add_info_to_list(self):
        nw_list = []  # the list were we will append all the keys
        for key in self.convert().items():  # iteration to do so
            nw_list.append(list(key))
        return nw_list

    # This method will print the network that is created

    def print_social_network(self):
        for var in range(len(self.social_network())):  # iteration t    o print the network
            print(f'{var} ->',*self.social_network()[var])