import requests
import html
import random

def get_questions(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises HTTPError for bad responses

        data = response.json()
        questions = data["results"]

        return questions

    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
        return None

def play_quiz(questions):
    score = 0

    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {html.unescape(question['question'])}")
        print("Category:", question['category'])

        # Combine all possible answers and shuffle them
        all_answers = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(all_answers)

        # Decode HTML entities and enumerate the answers for the user to choose
        for idx, answer in enumerate(all_answers, 1):
            print(f"{idx}. {html.unescape(answer)}")
        
        # Get user's answer
        try:
            user_answer = int(input("\nYour answer (1-4): "))
            if all_answers[user_answer - 1] == question['correct_answer']:
                print("Correct!\n")
                score += 1
            else:
                print("Incorrect!")
                print(f"The correct answer was: {html.unescape(question['correct_answer'])}\n")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a number from 1 to 4.\n")

        print("=" * 50)

    print(f"Quiz complete! Your score is {score}/{len(questions)}")

# The API URL
api_url = "https://opentdb.com/api.php?amount=10&type=multiple"

# Fetching the questions
questions = get_questions(api_url)

# Playing the quiz
if questions:
    play_quiz(questions)
else:
    print("No questions were retrieved.")