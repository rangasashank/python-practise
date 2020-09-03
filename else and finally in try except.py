f1= open("sashi.txt")

try:
    f = open("doesnot.txt")

except Exception as e:
    print(e)

else:
    print("this will run only if except is not running")

finally:
    print("run this anyway..")
    # f.close()
    f1.close()
print("impotant stuff")