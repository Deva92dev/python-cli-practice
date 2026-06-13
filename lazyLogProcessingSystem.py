def get_correct_level():
    while True:
        level = input("What is the current level?: ")
        cleaned_level = level.strip()

        if cleaned_level == "":
            print("You have put empty level, please try again")
            level = cleaned_level
            continue

        if not cleaned_level.isalpha():
            print("Please include only letters")
            continue

        if not cleaned_level.isupper():
            print("Level must be in uppercase")
            continue

        return cleaned_level


def get_correct_message():
    while True:
        message = input("What is the current message?: ")
        cleaned_message = message.strip()

        if cleaned_message == "":
            print("Message is empty, please write")
            message = cleaned_message
            continue

        if cleaned_message.isspace():
            print("Message must include whitespaces between words in string")
            message = cleaned_message
            continue

        return cleaned_message


def create_log_entry(level, message):
    return {"level": level, "message": message}


def get_high_severity_logs(logs):
    all_high_severity_logs = [
        item["message"] for item in logs if "WARNING" in item["level"]
    ]
    return all_high_severity_logs


def generate_errors(logs):
    for item in logs:
        if "ERROR" in item["level"]:
            yield item["message"]


def all_error_messages(logs):
    all_errors = (item["message"] for item in logs if "ERROR" in item["level"])
    print("all errors", list(all_errors))


def get_log_search(logs, level):
    search_item = {item["message"] for item in logs if item["level"] == level}
    return search_item


def get_unique_logs(logs):
    unique_logs = {item["level"] for item in logs}
    return unique_logs


def print_summary(text, value):
    print(text, value)


def log_execution(func):
    def inner(all_logs):
        print("Running get error count")

        func(all_logs)
        print("Finished get error count")

    return inner


@log_execution
def get_error_count(logs):
    errors = [item["level"] for item in logs if "ERROR" in item["level"]]
    errors_count = len(errors)
    print(errors_count)


def main():
    all_logs = []
    while True:
        cleaned_level = get_correct_level()
        cleaned_message = get_correct_message()

        log = create_log_entry(cleaned_level, cleaned_message)
        all_logs.append(log)
        for error in generate_errors(all_logs):
            print_summary("generating error messages: ", error)

        print_summary("all logs are: ", all_logs)

        all_error_messages(all_logs)
        all_high_severity_logs = get_high_severity_logs(all_logs)
        print_summary("severity logs", all_high_severity_logs)

        search_all_logs = input("Type level to search logs: ")
        search_logs = get_log_search(all_logs, search_all_logs)
        print_summary("Your searched logs are: ", search_logs)

        unique_logs = get_unique_logs(all_logs)
        print_summary("unique logs are: ", unique_logs)

        get_error_count(all_logs)


if __name__ == "__main__":
    main()
