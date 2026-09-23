def getInteger():
    while True:  #gets two integers
        x = input("What is the number ")
        try: 
            y = int(x)
            return y
        except: 
            x = input("What is the number ")

x = getInteger()
y = getInteger()
z = x+y
print(f"{x}+{y}={z}") #or # print(str(x)+ "+" + str(y) + "=" + str(z))