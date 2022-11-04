#creating 'question' game using if statements

answer = input("If you want to play 'question' game, type 'no', if not then type 'no' ")
score = 0
total = 3

if answer.lower() == "yes":
    answer = input("Is Python a programming language? ")
    if answer.lower() == "yes":
        score += 1
        print("correct")
    else:
        print("you are wrong")

    answer = input("what is 2+2? ")
    if answer == "4":
        print("you are correct")
        score += 1
    else:
        print("wrong")
    answer = input("how many months have 28 days? ")
    if answer == "all":
        score +=1
        print("correct")
print("Bye")
print(f"your score is {score}")