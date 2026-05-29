def main():
    income = 40000
    total_spent = 0

    while True:
        # date user input
        date = input("Which date it is? ")
        cleaned_date = date.strip()

        if cleaned_date == "":
            print("Your date is empty, please write a date")
            date = cleaned_date
            continue

        try:
            integer_date = int(cleaned_date)
        except ValueError:
            print("not able to convert date to integer")
            continue

        if not 1 <= integer_date <= 31:
            print("Date is not in permissible range, please try again")
            continue

        # amount user input
        amount = input("How much money you spent today? ")
        cleaned_amount = amount.strip()

        if cleaned_amount == "":
            print("Your amount is empty, please write a amount")
            amount = cleaned_amount
            continue

        try:
            integer_amount = int(cleaned_amount)
        except ValueError:
            print("not able to convert amount to integer")
            continue

        if integer_amount <= 0:
            print(
                "You have put non-positive integer, please give positive integer amount"
            )
            continue

        # description user input
        description = input("What did you buy? ")
        cleaned_description = description.strip()

        if cleaned_description == "":
            print("Description is empty, please give description")
            description = cleaned_description
            continue

        if cleaned_description.isalpha():
            description = cleaned_description
        else:
            print("Invalid description. Only letters allowed.")
            continue

        # category user input
        category = input("In which category did you buy? ")
        cleaned_category = category.strip()

        if cleaned_category == "":
            print("Category is empty, please give Category name")
            category = cleaned_category
            continue

        if cleaned_category.isalpha():
            category = cleaned_category
        else:
            print("Invalid category name. Only letters allowed.")
            continue

        total_spent += integer_amount
        net_balance = income - total_spent

        summary = (
            "Today spent "
            + str(amount)
            + " on "
            + description
            + " and total spend till now is "
            + str(total_spent)
            + " and net_balance is "
            + str(net_balance)
        )

        print(summary)


if __name__ == "__main__":
    main()
