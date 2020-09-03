#Name Printer
#Uses the print function to print the users name
a = input("Input your name then press enter: ")
#Asks for input of the persons name and stores it in a value

print("Nice to see you " + a + "!")
#Prints a phrase then the persons name then the final character to make a complete sentence
if a == "Calvin" or a == "calvin":
    #checks if name is the person
    print('Favorite quote: "Learn continually - there\'s always "one more thing" to learn! -Steve Jobs')
    #prints their favorite quote
else:
    #If name is not calvin it does this
    print('Sorry! ' + '"' + a + '"' + ' isn\'t in our database for favorite quotes. Have a nice day ' + a + '!')
    #Prints apology


input("\n\nPress the enter key to exit.")
#Allows the user to exit by pressing enter
