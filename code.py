import requests
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

# L'URL de l'API
api_url = "https://opentdb.com/api.php?amount=10"

# Récupération des questions
questions = get_questions(api_url)

# Affichage des questions
score = 0
if questions:
    for i, question in enumerate(questions, 1):
        question['incorrect_answers'].append(question['correct_answer'])
        random.shuffle(question['incorrect_answers'])
        print(f"Category: {question['category']}")
        print(f"Question: {question['question']}")
        print(f"Possible Answers: {', '.join(question['incorrect_answers'])}")
        user_answer = input('Your answer :')
        if user_answer == question['correct_answer']:
            score += 1
            print('Well done !!')
        else:
            print(f'Nice try... The correct answer was {question['correct_answer']} !')
        print(f'Your score is {score}/{i}')
        input('Press Enter to move on !')
        print("\n" + "="*50 + "\n")
else:
    print("No questions were retrieved.")

print(f'Your score: {score}/10')