
# This is a new python file
# From this line onward, the file will be centered around the Chat Bot program

#Implement more advanced functions
#Use conditionals and boolean logic to control prompts and responses
#Use lists to store and manipulate responses
#Use loops to check for input
#Use an imported function from a built-in module


#Create a function called get_bot_response(). This function must:

#It should have 1 parameter called user_response, which is a string with the users input.

#It should return a string with the chat bot’s response.

#It should use at least 2 lists to store at least 3 unique responses to different user inputs. For example, if you were building a mood bot and the user entered “happy” for how they were feeling your happy response list could store something like “I’m glad to hear that!”, “Yay!”, “That is awesome!”.

#Use conditionals to decide which of the response lists to select from. For example: if a user entered “sad”, my program would choose a reponse from the of sad response list. If a user entered “happy”, my program would choose a reponse from the of happy response list.

#Use choice() to randomly select one of the three responses. (See example from class.)

#Greet the user using print() statements and explain what the chat bot topic is and what kind of responses it expects.

#Get user input using the input() function and pass that user input to the get_bot_response() function you will write

#Print out the chat bot’s response that is returned from the get_bot_response() function

#Use a while() loop to keep running your chat bot until the user enters "done".
from random import choice 

def get_bot_response(user_response):
    bot_response_chevy = ["with an LS V8? Awesome!", "Camaro's and Corvettes, what a duo", "Huzzah! A Person of Quality!"]
    bot_response_ford = ["Watch out for those crowds!", "The original pony car", "Nothin is better than a '68 Eleanor"]
    bot_response_dodge = ["The All American Muscle Car", "707 hp Hellcat Engine? Yes please!", "No replacement for displacement"]


    if user_response == "chevy":
        return choice(bot_response_chevy)
    elif user_response == "ford":
        return choice(bot_response_ford)
    elif user_response == "dodge":
        return choice(bot_response_dodge)
    else:
        return "Ehhhhh I dont count that as American Muscle"

print("Welcome! Please enter your favorite American Muscle Car manufacturer")

user_response = ""
while True:
    user_response = input("What is your favorite American Muscle Car manufacturer?: ")

