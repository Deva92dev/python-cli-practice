def get_valid_date():
    while True:
        date = input("What is the day today?: ")
        cleaned_date = date.strip()

        if cleaned_date == "":
            print("Date is empty, please try again")
            date = cleaned_date
            continue

        try:
            integer_date = int(cleaned_date)
        except ValueError:
            print("date conversion failed, please try again")
            continue

        if not 1 <= integer_date <= 31:
            print("Date is not permissible range, please try again")
            continue

        return integer_date


def get_valid_amount():
    while True:
        amount = input("How much did you spend today?: ")
        cleaned_amount = amount.strip()

        if cleaned_amount == "":
            print("Amount is empty, please try again")
            amount = cleaned_amount
            continue

        try:
            integer_amount = int(cleaned_amount)
        except ValueError:
            print("Amount conversion failed, please try again")
            continue

        if integer_amount <= 0:
            print("Amount is non positive, please provide positive amount")
            continue

        return integer_amount


def get_valid_category():
    while True:
        category = input("In which category did you spend money?: ")
        cleaned_category = category.strip()

        if cleaned_category == "":
            print("Category is empty, please try again")
            category = cleaned_category
            continue

        if not cleaned_category.isalpha():
            print("Category must contain only letters, please try again")
            continue

        return cleaned_category


def get_valid_description():
    while True:
        description = input("On what did you spend money?: ")
        cleaned_description = description.strip()

        if cleaned_description == "":
            print("Description is empty, please try again")
            description = cleaned_description
            continue

        if not cleaned_description.isalpha():
            print("Description must contain only letters, please try again")
            continue

        return cleaned_description


def create_expense_entry(
    integer_date, integer_amount, cleaned_category, cleaned_description
):
    return {
        "date": integer_date,
        "category": {
            cleaned_category: {
                "amount": integer_amount,
                "description": cleaned_description,
            }
        },
    }


def search_category(expense, single_category):
    number_of_categories = []
    for item in expense:
        for _, val in item.items():
            if not isinstance(val, int):
                for key, new in val.items():
                    if key in number_of_categories:
                        pass
                    else:
                        number_of_categories.append(key)
                    if key == single_category:
                        print(f"amount spent on {key} is: ", new["amount"])

    return number_of_categories


def get_category_total(expense):
    category_total = 0
    all_expenses = []
    for item in expense:
        for _, val in item.items():
            if not isinstance(val, int):
                for _, new in val.items():
                    for _, anew in new.items():
                        if not isinstance(anew, str):
                            all_expenses.append(anew)
                            category_total += anew

    all_expenses.sort()
    largest_expense = all_expenses[-1]

    return category_total, largest_expense


def get_daily_expenditure(expense):
    everyday_expenses = []
    for item in expense:
        for _, val in item.items():
            if not isinstance(val, dict):
                today_date = val
            if not isinstance(val, int):
                for _, value in val.items():
                    today_spent = value["amount"]
                    today_expense = f"Amount spent on {today_date} is {today_spent}"
                    everyday_expenses.append(today_expense)

    return everyday_expenses


def print_values(text, value):
    print(f"{text}{value}")


def main():
    expense = []

    while True:
        integer_date = get_valid_date()
        integer_amount = get_valid_amount()
        cleaned_category = get_valid_category()
        cleaned_description = get_valid_description()

        entry = create_expense_entry(
            integer_date, integer_amount, cleaned_category, cleaned_description
        )

        single_category = input("Search By category... ")

        expense.append(entry)
        category_total, largest_expense = get_category_total(expense)
        number_of_categories = search_category(expense, single_category)
        everyday_expenses = get_daily_expenditure(expense)

        print_values("expenses are: ", expense)
        print_values("", everyday_expenses)
        print_values("number of categories are: ", len(number_of_categories))
        print_values("Category total is: ", category_total)
        print_values("largest expense is: ", largest_expense)


if __name__ == "__main__":
    main()
