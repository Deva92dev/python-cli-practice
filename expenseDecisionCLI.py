def main():
    income = 50000
    expense = []
    entry = {}
    days = []

    while True:
        date = input("What is the date today?: ")
        cleaned_date = date.strip()

        # use date input
        if cleaned_date == "":
            print("Your date is empty, please try again")
            date = cleaned_date
            continue

        try:
            integer_date = int(cleaned_date)
        except ValueError:
            print("date conversion failed, please try again")
            continue

        if not 1 <= integer_date <= 31:
            print("Your date is not in permissible range, please try again")
            continue

        # user amount input
        amount = input("How much did you spend today?: ")
        cleaned_amount = amount.strip()

        if cleaned_amount == "":
            print("Your amount is empty, please try again")
            amount = cleaned_amount
            continue

        try:
            integer_amount = int(cleaned_amount)
        except ValueError:
            print("amount conversion failed, please try again")
            continue

        if integer_amount <= 0:
            print("Your amount is no positive, please write positive amount")
            continue

        if integer_amount < 100:
            print("Small expense, very good!")
        elif 100 <= integer_amount < 500:
            print("Medium expense, you could have spend less")
        else:
            print("High expense, spend less, be happy")

        # user category input
        category = input("In which category did you spend?: ")
        cleaned_category = category.strip()

        if cleaned_category == "":
            print("Your category is empty, please try again")
            category = cleaned_category
            continue

        if cleaned_category.isalpha():
            category = cleaned_category
        else:
            print("category must contain only letters")
            continue

        # user description input
        description = input("On what did you spend money?: ")
        cleaned_description = description.strip()

        if cleaned_description == "":
            print("Your description is empty, please try again")
            description = cleaned_description
            continue

        if cleaned_description.isalpha():
            description = cleaned_description
        else:
            print("description must contain only letters")
            continue

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
        print("expense: ", expense)
        # monthly health status

        # reports
        category_keys = []
        category_amount = []
        for item in expense:
            new_cat = item["category"]
            for key in new_cat.keys():
                category_keys.append(key)
            for val in new_cat.values():
                category_amount.append(val["amount"])
                print(key, val["amount"])

        category_totals = sum(
            list(d["category"].values())[0]["amount"] for d in expense
        )
        largest_Expense = max(
            list(d["category"].values())[0]["amount"] for d in expense
        )
        print("The largest amount is: ", largest_Expense)
        print("The category total is: ", category_totals)

        today_date = list(d["date"] for d in expense)
        days.append(today_date)
        total_num_of_days = len(days)
        daily_spending = category_totals / total_num_of_days
        if daily_spending <= 1000:
            print("Your daily expenditure are good")
        elif 1000 < daily_spending <= 5000:
            print("Warning! Your daily spending is touching danger zone")
        else:
            print("Your daily expenditure is critical. Please review your finances.")

        monthly_spent = ((income - category_totals) / income) * 100
        if monthly_spent <= 1 / 4 * income:
            print("Your monthly spending is healthy")
        elif 1 / 4 * income < monthly_spent < 1 / 2 * income:
            print("Your monthly spending is moderate")
        elif monthly_spent >= 1 / 2 * income:
            print("Your monthly spending is high")


if __name__ == "__main__":
    main()
