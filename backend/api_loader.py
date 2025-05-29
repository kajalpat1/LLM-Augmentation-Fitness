import requests

def fetch_exercises(language_id=2, limit=50):
    url = f"https://wger.de/api/v2/exercise/?language={language_id}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    return data['results']

def save_exercises_to_txt(exercises, filename="data/workouts/wger_exercises.txt"):
    with open(filename, 'w') as f:
        for ex in exercises:
            f.write(f"Name: {ex['name']}\n")
            f.write(f"Description: {ex['description']}\n")
            f.write("\n---\n\n")