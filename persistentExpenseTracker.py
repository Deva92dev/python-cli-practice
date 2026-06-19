import json
import csv

file_path = (
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\expense.json"
)
csv_file_path = (
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\expense.csv"
)


def get_correct_date():
    while True:
        date = input("What is the date today?: ")
        cleaned_date = date.strip()

        if cleaned_date == "":
            print("date can not be empty")
            date = cleaned_date
            continue

        try:
            integer_date = int(cleaned_date)
        except ValueError:
            print("date conversion failed, please try again")
            continue

        if not 1 <= integer_date <= 31:
            print("date is not permissible range, please try again")
            continue

        return integer_date


def get_correct_amount():
    while True:
        amount = input("How much did you spend today?: ")
        cleaned_amount = amount.strip()

        if cleaned_amount == "":
            print("date can not be empty")
            amount = cleaned_amount
            continue

        try:
            integer_amount = int(cleaned_amount)
        except ValueError:
            print("date conversion failed, please try again")
            continue

        if integer_amount <= 0:
            print("Amount cannot be non positive, please try again")
            continue

        return integer_amount


def get_correct_category():
    while True:
        category = input("In what category did you spend money? ")
        cleaned_category = category.strip()

        if cleaned_category == "":
            print("Category can not be empty, please try again")
            continue

        if cleaned_category.isdigit():
            print("Category must contain only letters and spaces separating them")
            continue

        return cleaned_category


def get_correct_description():
    while True:
        description = input("On what did you spend money? ")
        cleaned_description = description.strip()

        if cleaned_description == "":
            print("Description can not be empty, please try again")
            continue

        if not cleaned_description.isalpha():
            print("description must contain only letters")
            continue

        return cleaned_description


def create_entry(date, amount, category, description):
    return {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description,
    }


def log_execution(func):
    def inner(*args):
        print("Decorator started running")
        result = func(*args)
        print("Decorator stooped running after getting the result")
        return result

    return inner


@log_execution
def load_expenses(file_path, expense):
    try:
        with open(file_path, "r") as file:
            result = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        result = []

    result.append(expense)

    return result


@log_execution
def save_expenses(result, file_path):
    try:
        with open(file_path, "w") as file:
            json.dump(result, file, indent=4)
    except FileNotFoundError:
        print("Can not find the file")


def search_expenses_by_category(expense, category):
    category_item = [item for item in expense if item["category"] == category]
    return category_item


def category_totals(expense, category):
    total_category_sum = sum(
        [d["amount"] for d in expense if d.get("category") == category]
    )
    return total_category_sum


def total_expenses(expense):
    total = sum(d["amount"] for d in expense)
    return total


def largest_expense(expense):
    largest = max(expense, key=lambda x: x["amount"])
    return largest


def generate_available_categories(expense):
    values = (item["category"] for item in expense)
    return values


def import_to_csv(expense):
    fieldnames = expense[0].keys()
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expense)


def main():
    date = get_correct_date()
    amount = get_correct_amount()
    category = get_correct_category()
    description = get_correct_description()

    expense = create_entry(date, amount, category, description)
    expenses = load_expenses(file_path, expense)

    all_categories = generate_available_categories(expenses)
    for item in all_categories:
        print("generating categories.. ", item)

    all_expenses = total_expenses(expenses)
    print("all expenses are", all_expenses)

    category_search = input("Search by category.. ")
    category_item = search_expenses_by_category(expenses, category_search)
    print(category_item)

    largest = largest_expense(expenses)
    print("Largest expense is: ", largest)

    total_category_sum = category_totals(expenses, category)
    print("Total category sum is: ", total_category_sum)
    print("Total number of expenses are: ", len(expenses))

    save_expenses(expenses, file_path)
    import_to_csv(expenses)


if __name__ == "__main__":
    main()
