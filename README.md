[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jwjr7VDL)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16917666)
# Lab 11 -  Flashcards

_Learning Objective: Demonstrate understanding of dictionaries_

This week we will be working on dictionaries, file input and string operations. If you have taken previous classes, you might recognize dictionaries as hash maps/tables. For everyone who hasn't seen them, they are basically look up tables, like our tradtional dictionaries.

You will be given a textfile called **"database.txt"** which has comma-separated values. This file has a key-value pair for flashcards. The first value is the question/term and the second item is the answer/defintion. 
You will use this file for input in your program to read in all the answers and questions and fill a dictionary with all these pairs.

After making the dictionary, you will iterate through all the "flashcards" by printing the question and then having the user hit "Enter" to see the answer. You should iterate through all the terms.

Finally, you will allow the user to enter any question and provide them with the answer. You will use the look-up function of dictionaries for this.


## Step 1: Create a dictionary

Create a fucntion called `build_dict(file_name)`. It takes a file_name string as parameter, and it returns a dictionary object whith the file content.

1) Opens up the file and iterates through each line
2) For EACH line:
   a) Separates the answer/question for each line based on a comma(",")
   b) Stores each answer and question appropriate in the dictionary
3) Returns the dictionary

## Step 2: Check the dictionary 

Create a function called `check_dict(key,dictionary)`. It takes in a string text to look up in the dictionary, 
and it returns the answer if found, or  "No match found" otherwise.

```
  IF term is in dictionary 
       Return answer
   ELSE
       Return "No match Found"
```

## Step 3: Create main

Create `main()` function
1) Build the dictionary by calling `build_dict(fileName)`
2) Iterate through dictionary(HINT: For Each loop)
   FOR EACH Key,Value Pair:
     print question
     prompt user to hit "Enter"
     print answer
3) WHILE User does not enter stop:
     Prompt user for a question/term to look up
     Call `check_dict(userInput)` and output return value


## Expected input and output
```
Let's review your flashcards!
Question: diversity
Press Enter to see the answer.
Answer:the practice or quality of including or involving people from a range of different social and ethnic backgrounds and of different genders/orientations
Press Enter for the next card.
Question: bias
Press Enter to see the answer.
Answer:cause to feel or show inclination or prejudice for or against someone or something
Press Enter for the next card.
Question: imposter syndrome
Press Enter to see the answer.
Answer:the experience of feeling like a phony—you feel as though at any moment you are going to be found out as a fraud
Press Enter for the next card.
Question: inclusion
Press Enter to see the answer.
Answer:a variety of people have a voice/power in decision-making or contributions
Press Enter for the next card.
Question: equity
Press Enter to see the answer.
Answer:fair treatment and opportunity for all people
Press Enter for the next card.

End of Deck. Redo all cards?(Y/N): N

Question Review time.
Enter Question(stop to end): error
Answer: No match found
Enter Question(stop to end): diversity
Answer: the practice or quality of including or involving people from a range of different social and ethnic backgrounds and of different genders/orientations
Enter Question(stop to end): bias
Answer: cause to feel or show inclination or prejudice for or against someone or something
Enter Question(stop to end): stop
End of Program.
```

## Test and Submit

There are no automated tests for this lab, so throughly test you program before submitting it.
As always, stop by student hours, send an email, check in with a peer, or stop by the STEM Center if you need any assistance.
