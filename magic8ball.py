import random
while True:
    answer = ["It is certain", "It is decidedly so", "Without a doubt",
            "Yes, definitely", "You may rely on it", "As I see it, yes",
            "Most likely", "Outlook good", "Yes", "Signs point to yes",
            "Reply hazy try again", "Ask again later",
            "Better not tell you now",
            "Cannot predict now", "Concentrate and ask again",
            "Don't count on it", "My reply is no", "My sources say no",
            "Outlook is not so good", "Very doubtful"]
    print(str("WELCOME TO MAGIC 8 BALL"))
    print(input("please, ask a question: "))
    print(str("...thinking..."))
    print()
    print()
    print(random.choice(answer))
    do_over = 1
    print("play again?")
    do_over = input("1 yes, 2 no: ")
    if do_over == str(2):
        break
