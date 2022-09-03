#This a program to generate a band name with info given by user.

#Create a greeting for the program.
print("Welcome to the band name generator.")

# Ask the user for the citythat grew up in and the name of the pet.
city = input("Which city did you grow up in?\n")
pet=input("Do you have pets? If yes, what is the name?\n")

#Combine the name od their city and the name of their pet to show them their band name.
print("Your band name could be " + city + " " + pet)