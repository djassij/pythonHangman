chances = 6 #Number of chances

#Returns True if the guessed letter is present in the word
#If letter is present in the word, adds it to the progress list
#Returns False otherwise
def guessIsRight(guess, word, progress):
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                progress[i] = guess
        return True
    else:
        return False

#Requests the category of the word
category = input("What is the category of your word? ")

#Creates a list of the letters in the word that one will guess
word = list(input("What is the word that you want someone to guess? "))

#Stores the length of the word in length
length = len(word)

#Assigns underscores to unguessed indices in the progress list
progress = []
for i in range(length):
    progress.append("_")

#Prints 100 spaces so that no one can see the word that was input
for i in range(100):
    print(" ")

#Prints directions, category and length of word
print("Welcome to Hangman! Your objective is to guess the word based on a topic. You have to guess each letter individually, and you can only make a maximum of six mistakes. The category is " + category + ". The word has " + str(length) + " letters.")

#-----------------------Primary Loop----------------------------#
while chances > 0:
    if "".join(progress) == "".join(word):
        print("Congratulations! You guessed the word!")
        break
    guess = input("What is your guess? ") #Asks for new guess
    
    if guessIsRight(guess, word, progress): 
        print("That letter is in the word! Here is what you have so far:")
        string = ""
        for i in range(len(progress)):
            string += progress[i]
        print(string)
        continue
    
    elif chances == 1:
        print("You are all out of guesses! The correct word is " + "".join(word) + ".")
        break
    
    else:
        chances -= 1
        print("That letter is not in the word! You have " + str(chances) + " chances left.")
        continue

