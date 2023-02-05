def hello():
    print("Hello, welcome to the age in seconds program! ")

def age_in_sec():
    user=int(input("Enter your age please: "))
    user_sec=user*365*24*60*60
    print(f"Your age in Second is {user_sec}.")

hello()
age_in_sec()
print("Goodbye!")

