import datetime
import json
import csv
import threading
import time

file_path = r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\logs.json"
csv_file_path = (
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\logs.csv"
)

all_file_path = [
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\logs.json",
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\logs2.json",
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\logs3.json",
]


def get_correct_level():
    while True:
        level = input("What is the level?: ")
        cleaned_level = level.strip()

        if cleaned_level == "":
            print("Level must not be empty, try again")
            level = cleaned_level
            continue

        if not cleaned_level.isalpha():
            print("Level must have only letters")
            continue

        if not cleaned_level.isupper():
            print("Level must be in uppercase letters.")
            continue

        return cleaned_level


def get_correct_message():
    while True:
        message = input("What is the message?: ")
        cleaned_message = message.strip()

        if cleaned_message == "":
            print("Message cannot be empty, please try again")
            message = cleaned_message
            continue

        if cleaned_message.isspace():
            print("Message must contain whitespace between words")
            continue

        return cleaned_message


def log_execution(func):
    def inner(*args):
        print("Decorator started running")
        result = func(*args)
        print("Decorator stooped running after getting the result")
        return result

    return inner


def load_json_logs(file_path, logs):
    try:
        with open(file_path, "r") as file:
            result = json.load(file)
            for every in result["all_logs"]:
                # double star unpack each dict
                log = LogEntry(**every)
                logs.all_logs.append(log)
    except (FileNotFoundError, json.JSONDecodeError):
        result = {}
        print("Error at loading files")

    return logs


def save_into_json_logs(logs, file_path):
    try:
        with open(file_path, "w") as file:
            json.dump(logs, file, cls=LogManagerEncoder, indent=4)
    except FileNotFoundError:
        print("File not found")


class LogEntry:
    def __init__(self, level, message, timestamp):
        self.level = level
        self.message = message
        self.timestamp = timestamp

    def __repr__(self):
        return (
            f"level: {self.level}, message: {self.message}, timestamp: {self.timestamp}"
        )

    def to_dict(self):
        return {
            "level": self.level,
            "message": self.message,
            "timestamp": self.timestamp,
        }

    def is_error(self):
        self.is_error = True

    def is_warning(self):
        self.is_warning = False


class LogManager:
    def __init__(self):
        self.all_logs = []

    def __iter__(self):
        for entry in self.all_logs:
            yield entry

    @log_execution
    def load_logs(self, level, message, timestamp):
        log = LogEntry(level, message, timestamp)
        self.all_logs.append(log)
        print(f"Log for {level} is added and current log entry is: {self.all_logs}")

    def search_logs(self, level):
        same_logs = [item for item in self.all_logs if item.level == level]
        return same_logs

    @log_execution
    def export_summary(self):
        warnings = get_all_warning(self)
        errors = get_all_errors(self)
        total_log_count = len(self.all_logs)
        warning = len(warnings)
        error = len(errors)
        key = get_most_common_level(self)

        print(total_log_count, warning, error, key[0])

        fieldnames = ["total", "errors", "warnings", "common"]
        values = {
            "total": total_log_count,
            "errors": error,
            "warnings": warning,
            "common": key[0],
        }

        with open(csv_file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(values)


class LogManagerEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj).__name__ == "LogManager" or "LogManager" in str(type(obj)):
            # it is in LogManager
            all_logs = []
            if hasattr(obj, "all_logs"):
                for entry in obj.all_logs:
                    all_logs.append(self._serialize_entry(entry))
            return {"type": "LogManager", "all_logs": all_logs}

        # Handle LogEntry instance if not already converted
        if type(obj).__name__ == "LogEntry" or "LogEntry" in str(type(obj)):
            return self._serialize_entry(obj)

        # handle datetime objects
        if isinstance(obj, datetime):
            return obj.isoformat()

        return super().default(obj)

    def _serialize_entry(self, entry):
        return {
            "level": entry.level,
            "message": entry.message,
            "timestamp": entry.timestamp,
        }


def generate_errors(logs):
    for each in logs.all_logs:
        new = each.to_dict()
        if new["level"] == "ERROR":
            yield each


def get_all_errors(logs):
    errors_all = [
        item for item in logs.all_logs if item.to_dict().get("level") == "ERROR"
    ]
    return errors_all


def get_all_warning(logs):
    all_warnings = [
        item for item in logs.all_logs if item.to_dict().get("level") == "WARNING"
    ]
    return all_warnings


def get_most_common_level(logs):
    all_levels = []
    for item in logs.all_logs:
        log = item.to_dict()
        all_levels.append(log["level"])

    counts = {}
    for item in all_levels:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    key, value = max(counts.items(), key=lambda item: item[1])
    return key, value


def process_log_file(path):
    print(f"Processing started for {path}")
    logs = LogManager()
    try:
        with open(path, "r") as file:
            result = json.load(file)
            for every in result["all_logs"]:
                log = LogEntry(**every)
                logs.all_logs.append(log)
        warnings = get_all_warning(logs)
        errors = get_all_errors(logs)
        print(
            f"Print summary : {len(warnings)} warnings,  {len(errors)} errors,  {len(logs.all_logs)} logs"
        )
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error at process log function")

    time.sleep(2)
    print(f"processing finished for {path}")


def main():
    all_logs = LogManager()
    level = get_correct_level()
    level_created_at = datetime.datetime.now()
    timestamp = level_created_at.timestamp()
    message = get_correct_message()

    all_logs.load_logs(level, message, timestamp)
    logs = load_json_logs(file_path, all_logs)
    print("Number of all logs is: ", len(logs.all_logs))

    search_single_log = input("Search your log... ")
    searched_logs = all_logs.search_logs(search_single_log)
    print(searched_logs)

    errors = generate_errors(logs)
    for each in errors:
        print("generating errors: ", each)

    whole_errors = get_all_errors(logs)
    print("All errors at once: ", whole_errors, len(whole_errors))

    all_warnings = get_all_warning(logs)
    print("Here are all warnings: ", all_warnings, len(all_warnings))

    get_most_common_level(logs)

    # create and stat thread
    t1 = threading.Thread(target=process_log_file, args=(all_file_path[0],))
    t2 = threading.Thread(target=process_log_file, args=(all_file_path[1],))
    t3 = threading.Thread(target=process_log_file, args=(all_file_path[2],))

    # start simultaneously
    t1.start()
    t2.start()
    t3.start()

    # wait them to complete
    t1.join()
    t2.join()
    t3.join()

    print("all tasks completed")

    save_into_json_logs(logs, file_path)
    all_logs.export_summary()


if __name__ == "__main__":
    main()
