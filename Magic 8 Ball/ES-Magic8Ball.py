"""play a magic 8 ball game."""
import random
import time

while True:
    answer = ["It is certain", "It is decidedly so", "Without a doubt",
              "Yes, definitely", "You may rely on it", "As I see it, yes",
              "Most likely", "Outlook good", "Yes", "Signs point to yes",
              "Reply hazy try again", "Ask again later",
              "Better not tell you now",
              "Cannot predict now", "Concentrate and ask again",
              "Don't count on it", "My reply is no", "My sources say no",
              "Outlook not so good", "Very doubtful"]
    number = random.randint(1, len(answer))
    print()
    print("Welcome to the Magic 8 Ball")
    question = input("Please ask a question: ")
    print("Thinking...")
    time.sleep(3)
    for i in range(len(answer)):
        if i == number:
            print(answer[i])
    again = 1
    print("Do you want to play again?")
    again = input("1 yes, 2 no: ")
    if again == str(2):
        break
