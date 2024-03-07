# The main is used to iterate and print everything that we have created in the classes.
# importing all the classes that we need from their files
from OpenFile import OpenFile
from Recommend import Recommand
from Display import Display

print("\033[1;42m  Hasan Ahmati")  #ANSI class code: 1 is to make the output bolt and 42 to make the background green
print("\033[1m ID:001259023")
print("Welcome to the social network")

while True:  #while is used so the program keep asking
    filename_input = input('Enter a filename for network data')  # there is the input used to enter the file name
    social = OpenFile(filename_input)   #object of the class so we can use the method open_file
    if not social.open_file():  #if the filename is not correct it will print the error message
        print('\033[1;41m The file that you entered does not exist,please enter a correct file name')
        continue
    else:  # else so the filename is correct it will continue to ask another question to display the network
        user_input = input(' Do you want to display the social network? (yes/no)?')

    while True:  # while is yet again used to keep asking
        if user_input == 'yes':  # if they want to display the social network it will print it
            social.print_social_network()
            break
        elif user_input == 'no':  # if its not it will break
            break
        elif user_input != 'no':  # if the input is other than yes and no it will ask another question
            user_input = input('\033[1;41m Please enter yes or no:')  # this is the other question
            continue

    user_input = input('Do you want to recommend a friend to a member(yes/no)?')  # the input for the other feature
    while True:
        if user_input == 'yes':  # if they want to recommend a friend they will be asked to enter the id
            enter_member = int(input('\033[1;42m Enter member ID: '))
            friend = Recommand(filename_input, enter_member)
            friend.recommandation_of_friends()  #from the id it will be printed the recommended friend
            user_input = input('Do you want to recommend friends to another user (y/n)?')  # the program keeps asking
            # if they want to recommend another friend but only after you firstly typed yes for the first question
            continue
        elif user_input == 'no':  #if they dont want to recommend a friend it will break
            break
        else:
            user_input = input('Plese enter yes or no')  # other condition is if they input something else than yes/no
            continue   # they will be asked to enter yes or no

    user_input = input('Display how many friends a particular person has (yes/no)?')  # this is needed for sub feature 3
    while True:
        if user_input == 'yes':  # if they want to display they will be askd another quesion
            enter_member = int(input('Enter member ID: '))
            get_mem_id = Display(filename_input, enter_member)  # this is the object of the class Display which has 2 arguments
            get_mem_id.display_nr_of_friends() # by calling the method the number of friends will be displayed
            break
        elif user_input == 'no':  # it continues with the other conditions
            break
        else:
            user_input = input('Enter yes or no')
            continue
 # the final one is if they want to try another network the program will repeat,if not it will break there
    display = input('Do you want to try another social network (yes/no)?')
    if display == "yes":
        display = True
    if display == "no":
        print("Thank you!")
        break