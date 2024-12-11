import json

def save_quiz(data, filename="quiz_data.json"):
    """Save quiz data to a file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_quiz(filename="quiz_data.json"):
    """Load quiz data from a file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def admin_menu():
    """Admin menu to manage quizzes."""
    quiz_data = load_quiz()
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Delete Question")
        print("4. Exit Admin Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            quiz_name = input("Enter quiz name: ")
            question = input("Enter the question: ")
            options = [input(f"Option {i + 1}: ") for i in range(4)]
            correct_option = int(input("Enter the correct option number (1-4): "))

            if quiz_name not in quiz_data:
                quiz_data[quiz_name] = []

            quiz_data[quiz_name].append({
                "question": question,
                "options": options,
                "answer": correct_option
            })
            save_quiz(quiz_data)
            print("Question added successfully!")

        elif choice == "2":
            for quiz, questions in quiz_data.items():
                print(f"\nQuiz: {quiz}")
                for i, q in enumerate(questions, 1):
                    print(f"{i}. {q['question']}")

        elif choice == "3":
            quiz_name = input("Enter quiz name: ")
            if quiz_name in quiz_data:
                for i, q in enumerate(quiz_data[quiz_name], 1):
                    print(f"{i}. {q['question']}")
                question_num = int(input("Enter question number to delete: "))
                if 1 <= question_num <= len(quiz_data[quiz_name]):
                    quiz_data[quiz_name].pop(question_num - 1)
                    save_quiz(quiz_data)
                    print("Question deleted successfully!")
                else:
                    print("Invalid question number.")
            else:
                print("Quiz not found.")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    """User menu to take quizzes."""
    quiz_data = load_quiz()
    while True:
        print("\n--- User Menu ---")
        print("1. Take Quiz")
        print("2. Exit User Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            quiz_name = input("Enter quiz name: ")
            if quiz_name in quiz_data:
                score = 0
                for i, q in enumerate(quiz_data[quiz_name], 1):
                    print(f"\nQ{i}. {q['question']}")
                    for j, option in enumerate(q['options'], 1):
                        print(f"  {j}. {option}")
                    answer = int(input("Your answer (1-4): "))
                    if answer == q['answer']:
                        score += 1

                print(f"\nYou scored {score}/{len(quiz_data[quiz_name])}")
            else:
                print("Quiz not found.")

        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main function to run the program."""
    while True:
        print("\n--- Online Quiz Management System ---")
        print("1. Admin Menu")
        print("2. User Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_menu()
        elif choice == "2":
            user_menu()
        elif choice == "3":
              print("Goodbye !")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
