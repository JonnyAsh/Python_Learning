import time;

password=input("What is your password?")

while password!="1234":
    print("Error")
    time.sleep(10)
    password=input("What is your password?")

print("Password correct")