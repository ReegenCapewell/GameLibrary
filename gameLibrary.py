import os
import random
import time

wordList = ["hello", "rainbow", "recreate", "fresh", "blessed", "colourful", "testing"]
choiceList = ["Rock", "Paper", "Scissors"]
cardDeck = [1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]
userDeck = []
dealerDeck = []
userTotal = 0
global dealerTotal
counter = 0

#Main Menu Function
def mainMenu(userName):
    x = 0
    menuGreeting = print("Great name " + userName + "!")
    while x == 0:  #While loop to constantly check if a valid option has been entered
        menuAnswer = input("====================================\nTo play Higher or Lower press 1\nTo play Maths Challenge press 2\nTo play Rock Paper Scissors press 3\nTo play Word Scramble press 4\nTo play Pontoon press 5\nTo view the game rules press 6\nTo quit press 7\n====================================")
        if (menuAnswer == "1"):
            higherLower(userName, x)
            x = 1
        elif (menuAnswer == "2"):
            mathsChallenge(userName)
            x = 1
        elif (menuAnswer == "3"):
            RPS(userName)
            x = 1
        elif (menuAnswer == "4"):
            wordScramble(userName)
            x = 1
        elif (menuAnswer == "5"):
            pontoon()
            x = 1
        elif (menuAnswer == "6"):
            viewHelp()
            x = 1
        elif (menuAnswer == "7"):
            quit()
        else:  #Error handling for if an invalid input is entered
            print("Please enter a valid input (1-7)")
            mainMenu(userName);

#Higher or Lower game function
def higherLower(userName, x):
    guessCounter = 0
    y = 0
    print("Welcome, "+ userName + " to Higher or Lower!")
    randomNumber = random.randint (1, 100)
    print("I am thinking of a number between 1-100..")
    while y == 0: #While loop to keep looping until the number is guessed correctly
        guessedNumber = input("What is my number?: ")
        guessedNumberReal = int(guessedNumber) #Converts the users string input into an integer
        guessCounter = guessCounter + 1
        if (guessedNumberReal == randomNumber):
            print ("Congratulations! "+ userName + " guessed it in "+ str(guessCounter) + " guess(es). Well Done!")
            y=y+1
        elif (guessedNumberReal < randomNumber):
            print ("====================================\nguess higher\n====================================")
        elif (guessedNumberReal > randomNumber):
            print ("====================================\nguess lower\n====================================")
        else: #Error handling for an invalid input
            print ("Please enter a number between 1 and 100.")
    mainMenu(userName)

#Maths Challenge game function
def mathsChallenge(userName):
    questionCounter = 0
    userScore = 0
    while (questionCounter < 10): #While loop criteria set to match the number of questions (10) to be asked
        number1 = random.randint(1,10)
        number2 = random.randint(1,10)
        answer = number1 * number2
        question = print(str(number1)+"*"+str(number2))
        userGuess = int(input("Write answer here: ")) #Takes the input that the user enters and stores as an integer
        if (userGuess == answer): #if answer is correct
            print("Correct!")
            userScore = userScore + 1
            questionCounter = questionCounter + 1
        else: #if answer is incorrect
            print("Wrong!")
            questionCounter = questionCounter + 1
    print(userName+" scored "+str(userScore)+" out of 10!")
    return mainMenu(userName) #Once the game is over return the user back to the main menu

def wordScramble(userName): #word scramble game function
    wordGuessCounter = 1 #locally defined guess counter
    print("Welcome, "+ userName +" to Word Scramble!")
    wordRandIndex = random.randint(0, len(wordList)) #Randomly generates number within bounds
    w = 0
    while (w == 0):
        chosenWord = random.choice(wordList) #randomly select a word in list
        print (''.join(random.sample(chosenWord, len(chosenWord)))) #scrambles word
        w = 1
    g = 0
    while (g == 0):
        guessedWord = input("What is the word?: ") #takes user input
        if (guessedWord == chosenWord): #if the user guesses the word correctly
            print("Congratulations, "+ userName + " you guessed the word in "+ str(wordGuessCounter) +" guess(es)!\n")
            g = 1
            userRestart = input("Do you want to play again?\nPress 1 to play again\nPress 2 to return to the main menu") #asks the user if they would like to restart the game
            if (userRestart == "1"):
                wordScramble(userName) #restarts the game
            elif (userRestart == "2"):
                return mainMenu(userName) #returns the user back to the main menu
        else: #Error handling
            print("That is not the word. Please try again.")
            wordGuessCounter = wordGuessCounter + 1 #increments the users guess count by 1

#Rock Paper Scissors start game function
def RPS(userName):
    print("Welcome, "+ userName + " to Rock Paper Scissors!")
    while (counter == 0): #Sets a while loop for until a valid option has been chosen
        userWeapon = input("==============================\nPress 1 for Rock\nPress 2 for Paper\nPress 3 for Scissors\n==============================\nChoose your weapon: ")
        if (userWeapon == "1"):
            userWeapon = "Rock" #Converts users selection into the appropriate weapon in Rock Paper Scissors
            aiRPSChoice(userWeapon)
            counter + 1 #Tells the loop that an option has been chosen
        elif (userWeapon == "2"):
            userWeapon = "Paper" #Converts users selection into the appropriate weapon in Rock Paper Scissors
            aiRPSChoice(userWeapon)
            counter + 1 #Tells the loop that an option has been chosen
        elif (userWeapon == "3"):
            userWeapon = "Scissors" #Converts users selection into the appropriate weapon in Rock Paper Scissors
            aiRPSChoice(userWeapon)
            counter + 1 #Tells the loop that an option has been chosen
        else: #Error Handling
            print ("Please enter a valid option. (1-3)")

#AI Opponents selection in Rock Paper Scissors function
def aiRPSChoice(userWeapon):
    userScore = 0
    compScore = 0
    aiChoice = random.choice(choiceList) #Picks one of the three possibilities at random
    if (aiChoice == "Rock"):
        print("========================\n" + aiChoice + " VS. " + userWeapon)
        if (userWeapon == "Rock"): #if both criteria are met then draw
            print ("Draw!")
            print (userName + " : " + str(userScore) + " == " + "Computer : " + str(compScore) + "\n========================") #displays the scores at the end of the current round
            restartGame() #restarts the game
        elif(userWeapon == "Paper"):
            print(userName + " Wins!") #if both criteria are met then user wins
            userScore = userScore + 1 #add 1 point to the users' score
            print (userName + " : " + str(userScore) + " == " + "Computer : " + str(compScore) + "\n========================") #displays the scores at the end of the current round
            restartGame()
        elif(userWeapon == "Scissors"): #if both criteria are met then the AI wins
            print("Computer Wins!")
            compScore = compScore + 1 #add 1 point to the AI score
            print (userName + " : " + str(userScore) + " == " + "Computer : " + str(compScore) + "\n========================") #displays the scores at the end of the current round
            restartGame() #restarts game
    elif (aiChoice == "Paper"):
        print("========================\n" + aiChoice + " VS. " + userWeapon)
        if (userWeapon == "Rock"):
            print ("Computer Wins!")
            compScore = compScore + 1
            print (userName + " : " + str(userScore) + " == " + "Computer : " + str(compScore) + "\n========================")
            restartGame()
        elif(userWeapon == "Paper"):
            print("Draw!")
            print (userName + " : " + str(userScore) + " == " + "Computer : " + str(compScore) + "\n========================")
            restartGame()
        elif(userWeapon == "Scissors"):
            print(userName + " Wins!")
            userScore = userScore + 1
            print (userName + " : " + str(userScore) + " == " + "Computer : " + str(compScore) + "\n========================")
            restartGame()
    else:
        print ("========================\n" + aiChoice + " VS. " + userWeapon)
        if (userWeapon == "Rock"):
            print (userName + " Wins!")
            userScore = userScore + 1
            print (userName + " : " + str(userScore) + " == " + "Computer : " + str(compScore) + "\n========================")
            restartGame()
        elif(userWeapon == "Paper"):
            print("Computer Wins!")
            compScore = compScore + 1
            print (userName + " : " + str(userScore) + " == " + "Computer : " + str(compScore) + "\n========================")
            restartGame()
        elif(userWeapon == "Scissors"):
            print("Draw!")
            print (userName + " : " + str(userScore) + " == " + "Computer : " + str(compScore) + "\n========================")
            restartGame()

#Rock Paper Scissors restart game function
def restartGame():
    rpsRestart = input("Do you want to play again?\nPress 1 to play again\nPress 2 return to the main menu") #takes user input
    if (rpsRestart == "1"):
        return RPS(userName) #restarts the game
    elif (rpsRestart == "2"):
        return mainMenu(userName) #returns the user back to the main menu
    else: #Error Handling for the input of invalid options
        print("Please enter a valid option. (1-2)")

#Welcome message
def pontoon():
    userDeck = [] #Makes sure the users' hand is empty at the start of a new round
    dealerDeck = [] #Makes sure the dealers' hand is empty at the start of a new round
    print("Welcome, "+ userName + " to Pontoon!")
    dealStartDeck(cardDeck, userDeck, dealerDeck) #deals the starting deck

#Deal cards at start of the game
def dealStartDeck(cardDeck, userDeck, dealerDeck):
    x = 0
    y = 0
    for x in range(2): #Loops to draw 2 cards
        card = random.choice(cardDeck) #randomly selects a card from the deck
        userDeck.append(card) #adds the chosen card to the users' deck
        cardDeck.pop(card) #removes the chosen card from the card deck
        print(userName+"'s Hand:")
        print(userDeck) # Displays the users' hand to the player
        print("")
    for y in range(2): #The same for the dealer as aboce (- displaying hand)
        dealerCard = random.choice(cardDeck)
        dealerDeck.append(dealerCard)
        cardDeck.pop(dealerCard)
    stickOrHit(cardDeck, userDeck, dealerDeck)

#Allows the user to take an extra card or not
def stickOrHit(cardDeck, userDeck, dealerDeck):
    userTotal = sum(userDeck) #Adds up total of users' hand
    print(userName+"'s Total: ")
    print(userTotal) #displays users' total to the player
    dealerTotal = sum(dealerDeck)#Adds up total of dealers' hand
    if (userTotal < 15):
        drawUserCard(cardDeck, userDeck, userTotal) #Draw another card if users' total is < 15
        if (dealerTotal < 15):
            drawDealerCard(cardDeck, dealerDeck, dealerTotal) #Draw another card if dealers' total is < 15
    elif (userTotal >= 15):
        userPontChoice = input("Do you want to Hit or Stick?:\nPress 1 for Hit\nPress 2 for Stick: ") #user input
        if (userPontChoice == "1"): #Draw another card for the user
            if (dealerTotal < 15):
                drawDealerCard(cardDeck, dealerDeck, dealerTotal) #If dealer total < 15 draw another card automatically
                drawUserCard(cardDeck, userDeck, userTotal)
            else:
                drawUserCard(cardDeck, userDeck, userTotal)
        elif (userPontChoice == "2"):
            if (dealerTotal < 15): #Call the end game function
                drawDealerCard(cardDeck, dealerDeck, dealerTotal)
                endGame(userDeck, dealerDeck, userTotal, dealerTotal)
            else:
                endGame(userDeck, dealerDeck, userTotal, dealerTotal)
        else:
            print("Please enter a valid option. (1-2)") #Error Handling
            stickOrHit(cardDeck, userDeck, dealerDeck)
    return (userTotal, dealerTotal)

#Draws a card (not a starting card) to the users' deck
def drawUserCard(cardDeck, userDeck, userTotal):
    newCard = random.choice(cardDeck) #Randomly selects a card from the deck
    userDeck.append(newCard) #Adds the chosen card to the users' deck
    cardDeck.pop(newCard) #Removes card from the deck
    print(userName+"'s Hand:")
    print(userDeck) #Display users' hand to player
    print("")
    userTotal = sum(userDeck)
    return stickOrHit(cardDeck, userDeck, dealerDeck) #Loop back to the stick or hit choice

#Draws a card (not a starting card) to the dealers' deck
def drawDealerCard(cardDeck, dealerDeck, dealerTotal):
    newCard2 = random.choice(cardDeck) #Randomly selects a card from the deck
    dealerDeck.append(newCard2) #Adds the chosen card to the dealers' deck
    cardDeck.pop(newCard2) #Removes the chosen card from the deck
    dealerTotal = sum(dealerDeck)

#Works out winner of game
def endGame(userDeck, dealerDeck, userTotal, dealerTotal):
    userTotal = sum(userDeck)
    dealerTotal = sum(dealerDeck)
    if (userTotal == dealerTotal): #if users total is the same as the dealers total
        print(userName+"'s Total")
        print(userTotal)
        print("")
        print("Dealer's Total")
        print(dealerTotal)
        print("")
        print("Draw!")
        pontoonRestart() #Runs the restart sequence
    elif (userTotal > dealerTotal): #if the users total is greater than the dealers total
        if (userTotal > 21): #checks to see if the user is over 21
            print("You Bust!")
            print(userName+"'s Total")
            print(userTotal)
            print("Dealer's Total")
            print(dealerTotal)
            pontoonRestart() # runs the restart sequence
    elif (userTotal < dealerTotal): #if the users total is less than the dealers total
            print("Dealer Wins!")
            print(userName+"'s Total")
            print(userTotal)
            print("Dealer's Total")
            print(dealerTotal)
            pontoonRestart()
    else: #else user total is less than dealers total
        print("Dealer Bust!")
        if (userTotal < 21):
            print(userName+"'s Total")
            print(userTotal)
            print("Dealer's Total")
            print(dealerTotal)
            print(userName+" Wins!")
            pontoonRestart()
        else:
            print(userName+"'s Total")
            print(userTotal)
            print("Dealer's Total")
            print(dealerTotal)
            print("Dealer Wins!")
            pontoonRestart()

#Pontoon restart sequence
def pontoonRestart():
    pontRestart = input("Do you want play again?\nPress 1 to play again\nPress 2 to return main menu") #asks user if they wish to play again
    if (pontRestart == "1"):
        pontoon() #restarts the game
    elif (pontRestart == "2"):
        mainMenu(userName) #returns the user to the main menu
    else: #error handling for the input of invalid options
        print("Please enter a valid option. (1-2)")

#Help section code
def viewHelp():
    helpChoice = input("Press 1 to view the rules of Higher or Lower\nPress 2 to view the rules of Maths Challenge\nPress 3 to view the rules of Rock Paper Scissors\nPress 4 to view the rules of Word Scramble\nPress 5 to view the rules of Pontoon\nPress 6 to return to the main menu\nAnswer Here: ")
    helpCounter = 0
    while helpCounter == 0:
        if (helpChoice == "1"):
            print("To play higher or lower simply enter a number between 1 and 100, (both the 1 and 100 are numbers that can be included.\nThe guesses must be whole numbers.)\n---------------------------------------\nYOU WILL BE RETURNED TO THE HELP SECTION MENU IN 30 SECONDS")
            time.sleep(30)
            viewHelp()
            helpCounter = 1
        elif (helpChoice == "2"):
            print("To play Maths Challenge answer the questions provided until the game is over.\nThere is no time limit\n* means multiplied.\n---------------------------------------\nYOU WILL BE RETURNED TO THE HELP SECTION MENU IN 30 SECONDS")
            time.sleep(30)
            viewHelp()
            helpCounter = 1
        elif (helpChoice == "3"):
            print("To play Rock Paper Scissors the following rules apply:\n - Press 1-3 to select either rock, paper or scissors\n - Rock > Scissors\n - Scissors > Paper\n - Paper > Rock\n---------------------------------------\nYOU WILL BE RETURNED TO THE HELP SECTION MENU IN 30 SECONDS")
            time.sleep(30)
            viewHelp()
            helpCounter = 1
        elif (helpChoice == "4"):
            print("To play Word Scramble simply enter the word you think is the scrambled word.\nThere are unlimited lives.\nThere is no time limit.\n---------------------------------------\nYOU WILL BE RETURNED TO THE HELP SECTION MENU IN 30 SECONDS")
            time.sleep(30)
            viewHelp()
            helpCounter = 1
        elif (helpChoice == "5"):
            print("The aim of the game in Pontoon is to get as close to a total of 21 with the hand of cards the player posseses.\nIf the 2 cards at the start of the round are below a total of 15 then an extra card is drawn automatically to the hand.\nTo stick with your current hand, when prompted press 1\nTo draw another card press 2.\n---------------------------------------\nYOU WILL BE RETURNED TO THE HELP SECTION MENU IN 30 SECONDS")
            time.sleep(30)
            viewHelp()
            helpCounter = 1
        elif (helpChoice == "6"):
            return mainMenu(userName)
        else:
            print("Please enter a valid option (1-6).")

#Main
userName = input("Hello there, what is your name?: ")
mainMenu(userName)
