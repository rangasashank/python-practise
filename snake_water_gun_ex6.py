import random
print("Welcome to snake water gun:\n")

i = 1

while i<=10:
    user_input = int(input("Choose 1 for snake, 2 for water, 3 for gun\n"))
    numberlist= ["snake", "water", "gun"]
    cpu_choice = random.choice(numberlist)
    print("You chose: " + str(user_input))
    cpuscore = 0
    userscore = 0
    
    
    if user_input == 1:
        if cpu_choice == "snake":
            print("The cpu chose snake")
            print("Its a tie")
            print("No. of chances used: " + str(i))
            print("No. of chances left: " + str(10 - i))
            a = 1

        elif cpu_choice == "water":
            print("The cpu chose water")
            print("You won")
            print("No. of chances used: " + str(i))
            print("No. of chances left: " + str(10 - i))
            a = 2


        elif cpu_choice == "gun":
            print("The cpu chose gun")
            print("cpu won")
            print("No. of chances used: " + str(i))
            print("No. of chances left: " + str(10 - i))
            a = 3


    
    elif user_input == 2:
        if cpu_choice == "water":
            print("The cpu chose water")
            print("Its a tie")
            print("No. of chances used: " + str(i))
            print("No. of chances left: " + str(10 - i))
            a = 1

        elif cpu_choice == "snake":
            print("The cpu chose snake")
            print("cpu won")
            print("No. of chances used: " + str(i))
            print("No. of chances left: " + str(10 - i))
            a = 3
            

        elif cpu_choice == "gun":
            print("The cpu chose gun")
            print("you won")
            print("No. of chances used: " + str(i))
            print("No. of chances left: " + str(10 - i))
            a = 2
            


    elif user_input == 3:
        if cpu_choice == "gun":
            print("The cpu chose gun")
            print("Its a tie")
            print("No. of chances used: " + str(i))
            print("No. of chances left: " + str(10 - i))
            a = 1

        elif cpu_choice == "snake":
            print("The cpu chose snake")
            print("you won")
            print("No. of chances used: " + str(i))
            print("No. of chances left: " + str(10 - i))
            a = 2
            
        elif cpu_choice == "water":
            print("The cpu chose water")
            print("cpu won")
            print("No. of chances used: " + str(i))
            print("No. of chances left: " + str(10 - i))
            a = 3
    else:
        int(input("Please choose only 1 for snake, 2 for water and 3 for gun\n"))
        continue
    i = i + 1

    
    if a == 1:
        userscore += 1 
        cpuscore += 1
    elif a == 2:
        userscore += 1
    elif a == 3:
        cpuscore += 1


if userscore > cpuscore:
        print("You won the game")
elif cpuscore > userscore:
        print("You loose the game")
else :
    print("Its a tie")

    

    


