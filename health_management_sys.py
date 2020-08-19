import datetime
def getdate():
    return datetime.datetime.now()
def take(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for diet"))
        if c==1:
            value = input("Enter the exercise:\n")
            with open("harry-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
                print("Successfully written!")
        
        elif c==2:
            value = input("Enter the diet:\n")
            with open("harry-d.txt", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
                print("Successfully written!")
        
        else:
            print("Please use only 1(exercise), 2(diet)")


    elif k == 2:
        c = int(input("enter 1 for exercise and 2 for diet"))
        if c==1:
            value = input("Enter the exercise:\n")
            with open("sashi-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
                print("Successfully written!")
        
        elif c==2:
            value = input("Enter the diet:\n")
            with open("sashi-d.txt", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
                print("Successfully written!")
        
        else:
            print("Please use only 1(exercise), 2(diet)")


    elif k == 3:
        c = int(input("enter 1 for exercise and 2 for diet"))
        if c==1:
            value = input("Enter the exercise:\n")
            with open("mark-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
                print("Successfully written!")
        
        elif c==2:
            value = input("Enter the diet:\n")
            with open("mark-d.txt", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
                print("Successfully written!")
        
        else:
            print("Please use only 1(exercise), 2(diet)")


    else:
        print("Please enter 1 for Harry, 2 for Sashi and 3 for Mark")


def get(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for diet"))
        if c==1:
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        
        elif c==2:
            with open("harry-d.txt") as op:
                for i in op:
                    print(i,end="")
        
        else:
            print("Please use only 1(exercise), 2(diet)")


    elif k == 2:
        c = int(input("enter 1 for exercise and 2 for diet"))
        if c==1:
            with open("sashi-ex.txt") as op:
                for i in op:
                    print(i,end="")
        
        elif c==2:
            with open("sashi-d.txt") as op:
                for i in op:
                    print(i,end="")
        
        else:
            print("Please use only 1(exercise), 2(diet)")


    elif k == 3:
        c = int(input("enter 1 for exercise and 2 for diet"))
        if c==1:
            with open("mark-ex.txt") as op:
                for i in op:
                    print(i,end="")
        
        elif c==2:
            with open("mark-d.txt") as op:
                for i in op:
                    print(i,end="")
        
        else:
            print("Please use only 1(exercise), 2(diet)")


    else:
        print("Please enter 1 for Harry, 2 for Sashi and 3 for Mark")

    
    
        






print("Health Management System:")
a = int(input("Press 1 to Lock value, Press 2 to Retrieve\n"))

if a==1:
    b = int(input("1 for Harry, 2 for Sashi, 3 for Mark"))
    take(b)
else:
    b = int(input("1 for Harry, 2 for Sashi, 3 for Mark"))
    get(b)
    