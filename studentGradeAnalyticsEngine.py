def get_valid_name():
    while True:
        name = input("What is your name?: ")
        cleaned_name = name.strip()

        if cleaned_name == "":
            print("Name is empty, please write your name")
            name = cleaned_name
            continue

        if not cleaned_name.isalpha():
            print("Name can not contain other than letters, please use letters only")
            continue

        return cleaned_name


def get_valid_score():
    while True:
        score = input("What is your score?: ")
        cleaned_score = score.strip()

        if cleaned_score == "":
            print("Score is empty, please write your score")
            score = cleaned_score
            continue

        try:
            integer_score = int(cleaned_score)
        except ValueError:
            print("Score conversion failed, please try again")
            continue

        if not 1 <= integer_score <= 100:
            print(
                "Score is not in permissible range, please write score between 1 and 100"
            )
            continue

        return integer_score


def create_student(name, score):
    return {"name": name, "score": score}


def get_average_score(students):
    total = 0
    for item in students:
        for _, val in item.items():
            if not isinstance(val, str):
                total += val

    average_score = round((total / len(students)), 2)
    return average_score


def get_maximum_score(students):
    scores = []
    for item in students:
        for _, val in item.items():
            if not isinstance(val, str):
                scores.append(val)

    scores.sort()
    maximum_score = scores[-1]
    return maximum_score


def get_minimum_score(students):
    scores = []
    for item in students:
        for _, val in item.items():
            if not isinstance(val, str):
                scores.append(val)

    scores.sort()
    minimum_score = scores[0]
    return minimum_score


def search_student_score(students, name):
    single_student = {
        item["name"]: item["score"] for item in students if item["name"] == name
    }
    return single_student


def get_high_performers(students):
    high_performers = [each for each in students if each["score"] >= 80]
    return high_performers


def get_low_performers(students):
    low_performers = [each["name"] for each in students if each["score"] < 40]
    return low_performers


def get_unique_grades(students):
    unique_grades = {item["score"] for item in students}
    return unique_grades


def process_item(d):
    if d["score"] >= 90:
        return "A"
    elif 80 <= d["score"] < 89:
        return "B"
    elif 70 <= d["score"] < 79:
        return "C"
    elif 40 <= d["score"] < 69:
        return "D"
    else:
        return "E"


def get_grade_bands(students):
    all_bands = {item["name"]: process_item(item) for item in students}
    return all_bands


def print_summary(text, value):
    print(text, value)


def main():
    students = []
    while True:
        cleaned_name = get_valid_name()
        integer_score = get_valid_score()

        entry = create_student(cleaned_name, integer_score)
        students.append(entry)
        print_summary("students", students)

        single_students = input("Search for Student...")

        average_score = get_average_score(students)
        maximum_score = get_maximum_score(students)
        minimum_score = get_minimum_score(students)
        single_student = search_student_score(students, single_students)

        high_performers = get_high_performers(students)
        low_performers = get_low_performers(students)
        unique_grades = get_unique_grades(students)
        all_bands = get_grade_bands(students)

        print_summary("Average score is: ", average_score)
        print_summary("Maximum score is: ", maximum_score)
        print_summary("Minimum score is: ", minimum_score)
        print_summary("Unique grades are: ", unique_grades)
        print_summary("Your score is: ", single_student)

        print_summary("These are low performers: ", low_performers)
        print_summary("These are high performers: ", high_performers)
        print_summary("here are the grade bands: ", all_bands)


if __name__ == "__main__":
    main()
