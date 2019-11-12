#Scenario
#The break statement is used to exit/terminate a loop
#Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters “Chupacabra” as the secret exit word.  In which case, the message “You’ve successfully left the loop.” should be printed to the screen, and the loop should terminate.
#Don’t print ANY of the words entered by the user.  Use the concept of conditional execution and the break statement. 
#start coding below here: some code is pre-filled for you.

#create the "secret_word" variable 
secret_word = ""

#start your while loop - which will run while something is True
while True:
  #create a "loop control variable" - a way for secret_word to be updated by user input()
  secret_word = input()
  #create a conditional argument - if the user enters “Chupacabra”, break out of the loop
  if secret_word == ('Chupacabra'):
    break
#print out a message to run after your loop is terminated.  “You’ve successfully left the loop.
print("you've successfully left the loop")
