from Graph import Graph
from person import Person
from App import SocialMediaApp

def SampleData():
    app = SocialMediaApp()

    # Create 5 sample users
    users_data = \
        [
        ("dylan", "Dylan Ng ", 21, "Male", "INFJ, gamer"),
        ("bob", "Bob Smith", 32, "Male", "Software engineer and gamer"),
        ("charlie", "Charlie Brown", 25, "Male", "Professional photographer"),
        ("diana", "Diana Prince", 30, "Female", "Chef and food blogger"),
        ("eve", "Eve Wilson", 27, "Female", "Digital artist")
        ]

    # Add users to the app
    for user_data in users_data:
        person = Person(*user_data)
        app.addUser(person)

    # Create sample connections
    connections = [
        ("dylan", "bob"),
        ("dylan", "diana"),
        ("bob", "dylan"),
        ("bob", "charlie"),
        ("charlie", "eve"),
        ("diana", "dylan"),
        ("eve", "charlie")
    ]

    for follower, followee in connections:
        app.followUser(follower, followee)

    return app


def displayUserProfile(user):
    # Display detailed profile of a user
    print(f"\n{'-' * 40}")
    print(f"PROFILE: @{user.user_id}")
    print(f"{'-' * 40}")
    print(f"Name: {user.name}")
    if user.age:
        print(f"Age: {user.age}")
    if user.gender:
        print(f"Gender: {user.gender}")
    if user.biography:
        print(f"Bio: {user.biography}")


def addNewUser(app):
    # Add a new user profile on-demand
    print(f"\n{'-' * 40}")
    print("ADD NEW USER PROFILE")
    print(f"{'-' * 40}")

    # Get user input for new profile
    user_id = input("Enter username (user ID): ").strip().lower()

    # Check if user ID already exists
    if app.getUser(user_id):
        print(f" Username '@{user_id}' already exists! Please choose a different username.")
        return False

    if not user_id:
        print(" Username cannot be empty!")
        return False

    name = input("Enter full name: ").strip()
    if not name:
        print(" Name cannot be empty!")
        return False

    # Optional fields
    age_input = input("Enter age (press Enter to skip): ").strip()
    age = None
    if age_input:
        try:
            age = int(age_input)
            if age < 1 or age > 120:
                print("Invalid age entered. Skipping age field.")
                age = None
        except ValueError:
            print("Invalid age format. Skipping age field.")
            age = None

    gender = input("Enter gender (press Enter to skip): ").strip()
    if not gender:
        gender = None

    biography = input("Enter biography (press Enter to skip): ").strip()
    if not biography:
        biography = ""

    # Create and add the new user
    new_person = Person(user_id, name, age, gender, biography)
    app.addUser(new_person)

    print(f"\n Successfully created new user profile:")
    displayUserProfile(new_person)
    return True


# main driver program
def main():
    print("Welcome to our Social Media Application!")
    app = SampleData()

    while True:
        print(f"\n{'=' * 50}")
        print("SOCIAL MEDIA APP - MENU")
        print(f"{'=' * 50}")
        print("1. Display all users")
        print("2. View user profile")
        print("3. View following list")
        print("4. View followers list")
        print("5. Add new user profile")
        print("6. Exit")
        print(f"{'=' * 50}")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            # Display all users
            print(f"\n{'-' * 30}")
            print("ALL USERS")
            print(f"{'-' * 30}")
            users = app.getAllUsers()
            for i, user in enumerate(users, 1):
                print(f"{i}. @{user.user_id} - {user.name}")

        elif choice == "2":
            # View user profile
            print(f"\n{'-' * 30}")
            print("VIEW USER PROFILE")
            print(f"{'-' * 30}")
            users = app.getAllUsers()
            for i, user in enumerate(users, 1):
                print(f"{i}. @{user.user_id} - {user.name}")

            try:
                user_choice = int(input("Select user number: ")) - 1
                if 0 <= user_choice < len(users):
                    displayUserProfile(users[user_choice])
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "3":
            # View following list
            print(f"\n{'-' * 30}")
            print("VIEW FOLLOWING LIST")
            print(f"{'-' * 30}")
            users = app.getAllUsers()
            for i, user in enumerate(users, 1):
                print(f"{i}. @{user.user_id} - {user.name}")

            try:
                user_choice = int(input("Select user number: ")) - 1
                if 0 <= user_choice < len(users):
                    selected_user = users[user_choice]
                    following = app.getFollowing(selected_user.user_id)
                    print(f"\n@{selected_user.user_id} is following:")
                    if following:
                        for user in following:
                            print(f"- @{user.user_id} ({user.name})")
                    else:
                        print("Not following anyone.")
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "4":
            # View followers list
            print(f"\n{'-' * 30}")
            print("VIEW FOLLOWERS LIST")
            print(f"{'-' * 30}")
            users = app.getAllUsers()
            for i, user in enumerate(users, 1):
                print(f"{i}. @{user.user_id} - {user.name}")

            try:
                user_choice = int(input("Select user number: ")) - 1
                if 0 <= user_choice < len(users):
                    selected_user = users[user_choice]
                    followers = app.getFollowers(selected_user.user_id)
                    print(f"\n@{selected_user.user_id} followers:")
                    if followers:
                        for user in followers:
                            print(f"- @{user.user_id} ({user.name})")
                    else:
                        print("No followers.")
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "5":
            # Add new user profile
            addNewUser(app)

        elif choice == "6":
            print("Thank you for using our Social Media Application!")
            break

        else:
            print("Invalid choice! Please select 1-6.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()