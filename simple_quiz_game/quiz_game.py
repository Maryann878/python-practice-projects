# 🧠 Simple Quiz Game

def quiz_game():
    print("🧠 Welcome to the Quiz Game!")
    score = 0

    questions = {
        "What is the capital of France? ": "paris",
        "Which planet is known as the Red Planet? ": "mars",
        "What is 5 + 7? ": "12"
    }

    for question, answer in questions.items():
        user_answer = input(question)
        if user_answer.lower() == answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {answer}.")

    print(f"\nYour final score is {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
