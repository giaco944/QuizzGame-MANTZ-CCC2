import requests

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
if questions:
    for i, question in enumerate(questions, 1):
        print(f"Question {i}:")
        print(f"Category: {question['category']}")
        print(f"Question: {question['question']}")
        print(f"Correct Answer: {question['correct_answer']}")
        print(f"Incorrect Answers: {question['incorrect_answers']}")
        print("\n" + "="*50 + "\n")
else:
    print("No questions were retrieved.")
