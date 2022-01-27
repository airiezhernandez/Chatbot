import random


#Question 1
name = str(input("What is your name? "))
print()
print("Hello!", name)
print()


#Question 2
age = int(input("How old are you? "))
print()
if (age > 18):
  print("Wow your an adult")
else:
  print("meow")


#Question 3
print()
color = str(input("What is your favorite color? "))
print()
if (color == "red"):
  print("My favorite color is red too!")
else:
  print("Red is my favorite color")



#Question 4
print()
game = str(input("What is your favorite game? "))
print()
if (game == "fortnite"):
  print("I hope your parents die")
  print()
else: 
  print("I like", game, "too")
  print()

#Question 5
n = random.randint(0,22)

choice = int(input("Guess my favorite number? "))
print()
if (choice == n):
  print("wow u got it right")
else: 
  print("Nope", n, 'is my favorite number')




