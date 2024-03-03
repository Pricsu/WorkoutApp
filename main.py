import json
import os

user_data = {}
if os.path.isfile("user_data.json"):
    with open("user_data.json", "r") as file:
        user_data = json.load(file)


def save_user_data():
    with open("user_data.json", "w") as file:
        json.dump(user_data, file, indent=2)


def create_user(username):
    if username in user_data:
        print("User is already exists")
    else:
        user_data[username] = {"workouts": [], "diet": []}
        save_user_data()


def log_workout(username, workout_name, date, duration):
    if username in user_data:
        user_data[username]["workouts"].append({"workout_name": workout_name,
                                                "date": date, "duration": duration})
        save_user_data()
    else:
        print("User doesn't exist")


def log_diets(username, meal_name, date, calories):
    if username in user_data:
        user_data[username]["diet"].append({"meal_name": meal_name, "date": date, "calories": calories})
        save_user_data()
    else:
        print("User doesn't exist")


def view_diet(username):
    if username in user_data:
        total_calories = sum([calorie["calories"] for calorie in user_data[username]["diet"]])
        print(f"User: {username}")
        print("Meals:")
        for j, i in enumerate(user_data[username]["diet"], start = 1):
            print(f"{j})  {i['meal_name']}  --   {i['date']}  --  {i['calories']}  ")
        print(f"Total calories: {total_calories}")
    else:
        print("Username doesn't exist")


def view_workout(username):
    if username in user_data:
        print(f"User: {username}")
        print("Workouts:")
        for j, i in enumerate(user_data[username]["workouts"], start = 1):
            print(f"{j})  {i['workout_name']}  --   {i['date']}  --  {i['duration']}  ")
    else:
        print("Username doesn't exist")


while True:
    print("""
1. Create User Profile
2. Log Diet
3. Log workout
4. View Diet
5. View Workout
6. Exit
    """)
    command = input("Enter your choice:")
    if command == "1":
        username = input("Enter your user name:")
        create_user(username)
    elif command == "2":
        username = input("Enter username: ")
        meal_name = input("Enter meal name: ")
        date = input("Enter date (YYYY-MM-DD): ")
        calories = int(input("Enter calories: "))
        log_diets(username, meal_name, date, calories)
    elif command == "3":
        username = input("Enter username: ")
        workout_name = input("Enter workout name: ")
        date = input("Enter date (YYYY-MM-DD): ")
        duration = float(input("Enter workout duration (minutes): "))
        log_workout(username, workout_name, date, duration)
    elif command == "4":
        username = input("Enter username: ")
        view_diet(username)
    elif command == "5":
        username = input("Enter username: ")
        view_workout(username)
    elif command == "6":
        break
    else:
        print("You entered a wrong command")