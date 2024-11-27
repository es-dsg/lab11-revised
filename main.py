'''
DEVELOPER: Julia De Guzman
COLLABORATORS: N/A
DATE: 11/11/2024
'''

"""
A one line summary of the program, terminated by a period.

This program quizzes and reviews flashcards.
"""

##########################################
# IMPORTS:
#   <list modules needed for program and their purpose>
##########################################
#<replace this line with import statement(s)>

##########################################
# FUNCTIONS:
##########################################
dict = {}
def build_dict(file_name): 
    """builds dictionary of cards and definitions based on values in database.txt. returns a dictionary of words/definitions"""
    fileObject = open(file_name,"r")
    for line in fileObject:
        key,value= line.split(",")
        dict[key.strip()] = value.strip()

    return dict    
    
def check_dict(key, dict): 
    """checks if word entered in main is in the dictionary. if it is it returns the corresponding value/definition. if it is not it returns "not found."""
    if key in dict:
        value=dict.get(key, "default")
        return value
    
    else:
        return("No match found.") 
        
##########################################
# MAIN PROGRAM:
##########################################

def main():
    pass
main()
build_dict("database.txt")
while(True):
    print("Let's review your flashcards!")
    for key in dict:
        print("Question:" + key)
        input("Press Enter to see the answer.")
        print("Answer:"+ dict.get(key,"default"))

    review = input("\nEnd of Deck. Redo all cards?(Y/N):")
    if review=="Y":
        True
    elif review =="N":
        break

print("Question Review time.")
while(True):
    key= input("Enter question(stop to end):")
    if key=="stop":
        print("End of program.")
        break
    else:
        print(check_dict(key, dict))
