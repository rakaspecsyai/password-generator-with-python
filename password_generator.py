import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
symbols = "!@#$%^&*()<>/"
number = "01234556789"

Use_for = lower_case + upper_case + symbols + number
password_length = 20

password = "".join(random.sample(Use_for, password_length))

print("your password: " + password)


question = input("Generate again? (y/n)")

while(True):
    new_password = "".join(random.sample(Use_for, password_length))
    print("your password: " + new_password)
    question = input("generate again? (y/n)")
    if(question == "n"):
        break
    elif(question != "n" and question != "y"):
        print("invalid answer")
        question = input("generate again? (y/n)")
        continue






