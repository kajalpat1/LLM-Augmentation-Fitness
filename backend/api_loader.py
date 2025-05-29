import os
import requests

def fetch_exercises(language_id=2, limit=50):
    url = f"https://wger.de/api/v2/exerciseinfo/?language={language_id}&limit={limit}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json().get('results', [])

def save_exercises_to_txt(exercises, filename="data/workouts/wger_exercises.txt"):

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f:
        for ex in exercises:
            trans = ex.get('translations', [])
            if trans:
                name        = trans[0].get('name',        'No name provided')
                description = trans[0].get('description', 'No description provided')
            else:
                name        = ex.get('name',        'No name provided')
                description = ex.get('description', 'No description provided')

            f.write(f"Name: {name}\n")
            f.write(f"Description: {description}\n")
            f.write("\n---\n\n")

if __name__ == "__main__":
    exs = fetch_exercises()
    print(f"Fetched {len(exs)} exercises.")
    if exs:
        print("Sample keys:", exs[0].keys())
    save_exercises_to_txt(exs)
    print("Wrote to data/workouts/wger_exercises.txt")


