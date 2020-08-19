n = 18
i = 1
total_guess = 10
while(i<=10):
    print("Guess the number\n")
    b = int(input())
    print("You have used " + str(i) + " number of chances")
    print("You have " + str(10-i) + " number of chances left")
    i += 1
    
    if b<18:
        print("the number you entered is smaller\n")
        continue
    if b>18:
        print("the number you entered is bigger\n")
        continue
    if b==18:
        print("Congrats you have guessed the number!\n")
        print("You have used "+ str(i) + " guesses to finish the game")
        break
print("Game Over!")


      