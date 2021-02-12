
'''

This file contains the functions that you need for completing this assignment. 

1. append_two_strings() --> Function to append a string2 to string1. -- 30%
2. append_character() --> Function to append a character to the end of string. -- 30% 
3. append_num_to_string() --> Function to append a number to the end of a string. -- 40%

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''

def append_two_strings(string_1, string_2):

    #print(f"String 1 Is: {string_1}")
    #print(f"String 2 Is: {string_2}")
    sum = input(string_1 + string_2)
    return sum
    


def append_character(string_1, char_1):

    #print(f"String 1 Is: {string_1}")
    #print(f"Character 1 Is: {char_1}")
    sum = input(string_1 + char_1)
    return sum
    


def append_num_to_string(string_1, num_1):

    #print(f"String 1 Is: {string_1}")
    #print(f"Number 1 Is: {num_1}")
    sum = input(string_1 + num_1)
    return sum


if __name__ == "__main__":
    
    string_1 = str(input("Enter 1st Word: "))
    string_2 = str(input("Enter 2nd Word: "))
    char_1 = str(input("Enter Character: "))
    num_1 = str(input("Enter Number: "))
    result = append_two_strings(string_1, string_2), append_character(string_1, char_1), append_num_to_string(string_1, num_1)
