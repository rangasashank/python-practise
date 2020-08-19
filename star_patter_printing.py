def str_pattern(a, b):
    i = 0
    if b == True:
        while(i<a):
            print((i+1)*('*')) 
            i +=1
           
    elif b == False:
        i = a
        while(i>0):
            print((i)*('*'))
            i = i-1
            
a = int(input("Enter the number of columns\n"))
c = int(input("Choose 0 or 1\n"))
b = bool(c)
d = str_pattern(a, b)

