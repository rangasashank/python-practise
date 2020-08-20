# def func_name_print(a, b, c, d):
#     print(a, b, c, d)

# 

def funargs(n, *args, **kwargs):
    print(n)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(f"{key} is {value}")

list = ["ab", "cd", "ef"]
dict = {"shiv":"cook", "sashi":"topper"}
n = "Good Morning" 
funargs(n, *list, **dict)