import csv

# # def main():
# #     user_input = input("What is user input? ")

# #     if not user_input:
# #         print("empty")
# #     else:
# #         print("not empty")


# # if __name__ == "__main__":
# #     main()


# # positive number validator,
# # def main():
# #     number_input = input("Please write positive number ")

# #     if number_input:
# #         positive_number = int(number_input)
# #         while positive_number <= 0:
# #             print("It is not positive number")
# #             positive_number = int(input("Please write positive number "))
# #         else:
# #             print("You have written positive number")
# #     else:
# #         print("error, please try again")


# # if __name__ == "__main__":
# #     main()


# # Exercise — Safe Integer Input System
# #  Input must not be empty, Input must not be only spaces , Input must successfully convert to integer, Integer must be positive
# # def main():
# #     while True:
# #         correct_input = input("Please give me correct input: ")
# #         cleaned_input = correct_input.strip()

# #         if cleaned_input == "":
# #             print("Your input is empty, please try again")
# #             correct_input = cleaned_input
# #             continue

# #         try:
# #             integer_input = int(cleaned_input)
# #         except ValueError:
# #             print("Not able to convert")
# #             continue

# #         if integer_input <= 0:
# #             print(
# #                 "You have put non-positive integer, please give positive integer input"
# #             )
# #             continue
# #         else:
# #             print(integer_input)
# #             break


# # if __name__ == "__main__":
# #     main()


# # dict dynamic nested values
# # food = 0
# # user = {"name": "deva", "expense": {"food": 500}}
# # val = user["expense"]["food"]
# # if val:
# #     food = 700
# #     val += food

# #     print(val)

# # expense = {}

# # while True:
# #     date = input("What is the date today?: ")
# #     category = input("What is the category?: ")
# #     amount = input("What is the amount?: ")
# #     description = input("What is the description?: ")

# #     expense = {
# #         "date": date,
# #         "category": {category: {"amount": amount, "description": description}},
# #     }

# #     amy = list(expense["category"].values())[0]
# #     mya = amy["amount"]

# #     print(mya)

# # new = [
# #     {"id": 1, "data": {"amount": 500, "color": "blue"}},
# #     {"id": 2, "data": {"amount": 700, "color": "yellow"}},
# #     {"id": 2, "data": {"amount": 300, "color": "blue"}},
# #     {"id": 2, "data": {"amount": 400, "color": "green"}},
# # ]
# # total_data_sum = sum(d["data"]["amount"] for d in new)
# # print(total_data_sum)
# # largest_sum = max(d["data"]["amount"] for d in new)
# # print(largest_sum)


# def main():
#     new = [
#         {"id": "Deva", "amount": 500},
#         {"id": "Peter", "amount": 700},
#         {"id": "Doe", "amount": 300},
#         {"id": "Amy", "amount": 400},
#     ]

#     def average(new):
#         scores = []
#         for item in new:
#             for _, val in item.items():
#                 if not isinstance(val, str):
#                     scores.append(val)

#         scores.sort()
#         largest = scores[-1]
#         return largest

#     largest


# if __name__ == "__main__":
#     main()


# # sum = new[0]["amount"]
# # print(sum)

# new = [
#     {"id": "Deva", "amount": 500},
#     {"id": "Peter", "amount": 700},
#     {"id": "Doe", "amount": 300},
#     {"id": "Amy", "amount": 400},
# ]
# all_amount = []
# for item in new:
#     hello = item["amount"]
#     all_amount.append(hello)


# print(all_amount)

# result = {item["id"]: item.get("amount", None) for item in new if id in item}


# single = []
# for item in new:
#     for _, val in item.items():
#         single.append(val)

# print(single)

# me = [each for each in new if each["amount"] >= 500]
# print(me)


# def hello():
#     data = [
#         {"level": "INFO", "message": "user logged in"},
#         {"level": "ERROR", "message": "database failed"},
#         {"level": "WARNING", "message": "disk space is running out"},
#         {"level": "INFO", "message": "user logged out"},
#         {"level": "ERROR", "message": "no server"},
#         {"level": "ERROR", "message": "no internet"},
#     ]

#     for item in data:
#         if "ERROR" in item["level"]:
#             yield item["message"]


# def main():
#     data = hello()
#     print(data)


# if __name__ == "__main__":
#     main()

# class examples
# class Car:
#     def __init__(self, distance, color):
#         self.distance = distance
#         self.color = color

#     def __str__(self):
#         return f"The {self.color} car has {self.distance} miles"


# car1 = Car(20000, "Blue")
# car2 = Car(30000, "Red")

# print(car1)
# print(car2)


# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# class Pitbull(Dog):
#     pass


# class Rotviller(Dog):
#     pass


# class German(Dog):
#     pass


# miles = Pitbull("miles", 4)
# teddy = Rotviller("teddy", 9)
# bruno = German("bruno", 5)


# print(teddy.speak("woof"))
# print(teddy.species)

# my_list = [
#     {"id": 1, "fruit": "apple"},
#     {"id": 2, "fruit": "banana"},
#     {"id": 3, "fruit": "kiwi"},
# ]

# # Remove dictionary where 'id' is 2
# my_list = [item for item in my_list if item.get("id") != 2]
# print(my_list)

# def get_correct_status():
#     while True:
#         status = input("Have you borrowed this book?: ")
#         cleaned_status = status.strip().lower()

#         if cleaned_status in ("true", "y", "yes", "yeah"):
#             return True
#         elif cleaned_status in ("false", "n", "no", "not"):
#             return False
#         else:
#             print("Invalid response. Please type 'True' or 'False'.")

# #         return cleaned_status

# level = os.path.isdir()
# print(level)

data = [
    {"date": 2, "amount": 800, "category": "Food", "description": "Pizza"},
    {"date": 5, "amount": 1000, "category": "Veg", "description": "Brinjal"},
    {"date": 16, "amount": 520, "category": "Veg", "description": "Tomato"},
    {"date": 19, "amount": 1600, "category": "Travel", "description": "Diesel"},
    {"date": 21, "amount": 5000, "category": "Shopping", "description": "Clothes"},
    {"date": 6, "amount": 700, "category": "Sports", "description": "Boll"},
    {"date": 8, "amount": 1300, "category": "Household", "description": "chores"},
    {"date": 26, "amount": 2500, "category": "Shopping", "description": "Pants"},
    {"date": 16, "amount": 1800, "category": "veg", "description": "Vegetables"},
    {"date": 19, "amount": 1650, "category": "Food", "description": "Burger"},
    {"date": 21, "amount": 1230, "category": "Vegetables", "description": "Potato"},
    {"date": 15, "amount": 1200, "category": "Food", "description": "Ice"},
    {"date": 8, "amount": 1235, "category": "Study", "description": "Books"},
    {"date": 23, "amount": 2560, "category": "Entertainment", "description": "Cinema"},
    {"date": 7, "amount": 120, "category": "Household", "description": "Soaps"},
    {"date": 12, "amount": 1500, "category": "veg", "description": "food"},
]

# total = [d["amount"] for d in data if "Food" in d["category"]]
# all_categories = {d["category"] for d in data}
# print(all_categories)
# print(sum(total))
# print(len(data))

# values = (item["category"] for item in data)
# for name in values:
#     print(name)

# total_sum = sum(d["amount"] for d in data if "Veg" in d.get("category") == "Veg")
# print(total_sum)

# largest = max(data, key=lambda x: x["amount"])
# print(largest)
csv_file_path = (
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\expense.csv"
)
fieldnames = data[0].keys()
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
