def main():
    income = 40000
    expense = []
    entry = {}
    total_spent = 0

    # date user inputs
    while True:
        date = input("What is the date today?: ")
        cleaned_date = date.strip()

        if cleaned_date == "":
            print("Your gave empty date input, please write date")
            date = cleaned_date
            continue

        try:
            integer_date = int(cleaned_date)
        except ValueError:
            print("Date conversion failed, try again")
            continue

        if not 1 <= integer_date <= 31:
            print("Your date is out of range, please write date in the range")
            continue

        # amount user input
        amount = input("How much did you spend today?: ")
        cleaned_amount = amount.strip()

        if cleaned_amount == "":
            print("You have written nothing, please write amount")
            amount = cleaned_amount
            continue

        try:
            integer_amount = int(cleaned_amount)
        except ValueError:
            print("amount conversion failed, please try again")
            continue

        if integer_amount <= 0:
            print("You have written non positive amount, please write actual amount")
            continue

        # category user input
        category = input("In which category did you buy?: ")
        cleaned_category = category.strip()

        if cleaned_category == "":
            print("You have given empty category input, please write")
            category = cleaned_category
            continue

        if cleaned_category.isalpha():
            category = cleaned_category
        else:
            print("category doesn't contain letters, please try again")
            continue

        # description user input
        description = input("What did you buy?: ")
        cleaned_description = description.strip()

        if cleaned_description == "":
            print("Your description is empty, please write")
            description = cleaned_description
            continue

        if cleaned_description.isalpha():
            description = cleaned_description
        else:
            print("Invalid description, only letters are allowed")
            continue

        if integer_date in expense:
            if entry["category"]:
                current_index = list(entry["category"].values())[0]
                current_amount = current_index["amount"]
                current_amount += integer_amount
                new_desc = cleaned_description + cleaned_description
                new_desc.replace("", ", ")
            else:
                entry["category"] = {
                    cleaned_category: {
                        "amount": integer_amount,
                        "description": cleaned_description,
                    }
                }

        else:
            entry = {
                "date": integer_date,
                "category": {
                    cleaned_category: {
                        "amount": integer_amount,
                        "description": cleaned_description,
                    }
                },
            }
            expense.append(entry)

        total_spent += integer_amount
        net_balance = income - total_spent
        print(expense)

        category_total = sum(list(d["category"].values())[0]["amount"] for d in expense)
        largest_amount = max(
            list(entry["category"].values())[0]["amount"] for entry in expense
        )
        print("category total: ", category_total)
        print("largest amount: ", largest_amount)
        print("total spent till now: ", total_spent)
        print("net balance remaining: ", net_balance)


if __name__ == "__main__":
    main()
