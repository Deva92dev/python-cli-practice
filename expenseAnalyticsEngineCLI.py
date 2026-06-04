def main():
    income = 50000
    expense = []
    entry = {}

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

        # amount
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

        # category
        category = input("In which category did you spend money?: ")
        cleaned_category = category.strip()

        if cleaned_category == "":
            print("Category is empty, please try again")
            category = cleaned_category
            continue

        if not cleaned_category.isalpha():
            print("Category must contain only letters, please try again")
            continue

        # description
        description = input("On what did you spend money?: ")
        cleaned_description = description.strip()

        if cleaned_description == "":
            print("Description is empty, please try again")
            description = cleaned_description
            continue

        if not cleaned_description.isalpha():
            print("Description must contain only letters, please try again")
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

        category_total = 0
        all_expenses = []
        expenses_for_filtering = []
        for item in expense:
            for _, val in item.items():
                if not isinstance(val, dict):
                    today_date = val
                if not isinstance(val, int):
                    for _, new in val.items():
                        first_key, first_value = next(iter(new.items()))
                        new_dict = {first_key: first_value}
                        expenses_for_filtering.append(new_dict)
                        for key, anew in new.items():
                            if not isinstance(anew, str):
                                all_expenses.append(anew)
                                print(f"Amount spent on {today_date} is: ", anew)
                                category_total += anew

        number_of_categories = []
        single_category = input("Search By category... ")
        for item in expense:
            for _, val in item.items():
                if not isinstance(val, int):
                    for key, new in val.items():
                        number_of_categories.append(key)
                        if key == single_category:
                            print(f"amount spent on {key} is: ", new["amount"])
                            continue

        all_expenses.sort()
        largest_expense = all_expenses[-1]
        print(expense)
        print("number of expenses", len(expense))
        print("number of categories: ", len(number_of_categories))
        print("largest expense is: ", largest_expense)
        print("Category totals: ", category_total)
        print("expenses for filtering: ", expenses_for_filtering)
        store_expenditure = []

        for expenditure in expenses_for_filtering:
            if expenditure["amount"] > 500:
                store_expenditure.append(expenditure)
                print("filtered expenditure above 500 : ", store_expenditure)
            elif 100 <= expenditure["amount"] <= 500:
                store_expenditure.append(expenditure)
                print("filtered expenditure between 100 to 500: ", store_expenditure)
            elif expenditure["amount"] < 100:
                store_expenditure.append(expenditure)
                print("filtered expenditure below 100: ", store_expenditure)


if __name__ == "__main__":
    main()
