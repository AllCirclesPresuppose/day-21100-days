print("Math Game!")
print()
print("Lets see how good your multiplication skills are!")
print("Input your number, and guess the correct answer from 1-10 times your number!")
print()
number = input("Name your multiples: ")
score = 0

for i in range(10):
    guess = input(str(i + 1) + " X " + str(number) + " = ")
    correct = (i + 1) * int(number)
    if int(guess) == int(correct):
        print("That's right!")
        score += 1
    else:
        print("Nope. The answer was " + str(correct))

print("you scored ", score, " out of 10.")
if score > 9:
  print("Way to go! You got them all right!")
elif score > 7:
  print("Not to shabby, got most of them right!")
elif score > 5:
  print("Hmm, may need to brush up a bit, but that's still passing!")
else:
  print("May need to go back to your math books friend!")
