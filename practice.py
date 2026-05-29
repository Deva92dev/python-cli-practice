# def main():
#     user_input = input("What is user input? ")

#     if not user_input:
#         print("empty")
#     else:
#         print("not empty")


# if __name__ == "__main__":
#     main()


# positive number validator,
# def main():
#     number_input = input("Please write positive number ")

#     if number_input:
#         positive_number = int(number_input)
#         while positive_number <= 0:
#             print("It is not positive number")
#             positive_number = int(input("Please write positive number "))
#         else:
#             print("You have written positive number")
#     else:
#         print("error, please try again")


# if __name__ == "__main__":
#     main()


# Exercise — Safe Integer Input System
#  Input must not be empty, Input must not be only spaces , Input must successfully convert to integer, Integer must be positive
def main():
    while True:
        correct_input = input("Please give me correct input: ")
        cleaned_input = correct_input.strip()

        if cleaned_input == "":
            print("Your input is empty, please try again")
            correct_input = cleaned_input
            continue

        try:
            integer_input = int(cleaned_input)
        except ValueError:
            print("Not able to convert")
            continue

        if integer_input <= 0:
            print(
                "You have put non-positive integer, please give positive integer input"
            )
            continue
        else:
            print(integer_input)
            break


if __name__ == "__main__":
    main()
