import random
#--------------------------------------------------------------------------------
#these stuffs
default_character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+|][;:.><,"
default_password_length = 20
max_len = 100
min_len = 1
#--------------------------------------------------------------------------------
#questions
desired_len_question = "how long your password should be?? [empty enter for default len]: "
desired_character_set_question = "Use the ASCII character set? [press Enter. " \
                                 "if no; enter some your self below]: "
should_continue_question = "do you want any other password to be genrated? (n,y): "
user_input_was_invalid = "InvalidUserInput"
sepration_line = "=========================="

should_continue_answer_True = "y"
should_continue_answer_False = "n"

#--------------------------------------------------------------------------------
def generate_password(ch_set, pass_len):
    output = ""
    for i1 in range(pass_len):
        output += random.choice(ch_set)
    return output

#--------------------------------------------------------------------------------
def ask_the_first_question():
    a = input(desired_len_question)


    if (a.isnumeric() is True):
        int_a = int(a)

    else:
        return default_password_length

    if int_a > max_len:
        print("given length is too big [max len is 100]")
        return default_password_length

    elif int_a < min_len:
        print("given lenght is less than zero >:(")
        return default_password_length

    else:
        return int_a
#--------------------------------------------------------------------------------
def ask_the_second_question():
    a = input(desired_character_set_question+"\n\b"+"->")
    b = "".join(list(set(a)))
    #   "".join(list(set(a)))  --> will elimintae repeated charcter
    #   for example aaaagabbbbbc will become agbc
    if len(a) == 0:
        return default_character_set

    elif len(b) >= 1:
        return b
#--------------------------------------------------------------------------------
def ask_if_wants_to_continue():
    a = input(should_continue_question)
    if a == should_continue_answer_True:
        return True

    elif a == should_continue_answer_False:
        return False

    else:
        return True
#--------------------------------------------------------------------------------
if __name__ == "__main__":

    should_continue = True
    while should_continue:

        first_question_answer = ask_the_first_question() #asking len of pass
        second_question_answer = ask_the_second_question() #aksing character set to use in pass

        print_this = generate_password( ch_set=second_question_answer , pass_len=first_question_answer )
        print("your password:")
        print(print_this)
        print(sepration_line)


        should_continue = ask_if_wants_to_continue()

        if should_continue == False:
            break

