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
def main():
    pass
main()
flashcards = build_dict("database.txt")
print("Let's review your flashcards!")

redo = "Y"
while redo == "Y" or redo == "y":
    for pair in flashcards.items(): #makes a tuple of questions and answers
        question, answer = pair
        print("Question:" + question)
        input("Press Enter to see the answer.")
        print("Answer:"+ answer)
        input("Press enter for the next card.")

    redo = input("\nEnd of Deck. Redo all cards?(Y/N):")

print("Question Review time.")
question = input("Enter question(stop to end):")
while(question != "stop"):
    print(check_dict(question, dict))
    question = input("Enter question(stop to end):")

print ("End of program.")

