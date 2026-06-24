import json
FILE_NAME = "sports_data.json"
def initialize_file():
    try:
        with open(FILE_NAME, "r") as file:
            json.load(file)
    except FileNotFoundError:
        data = {
            "favourite_teams": [],
            "match_notes": [],
            "generated_summaries": []
        }
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
    except json.JSONDecodeError:
        print("Corrupted file detected. Creating a new file.")
        data = {
            "favourite_teams": [],
            "match_notes": [],
            "generated_summaries": []
        }
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
def read_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        initialize_file()
        return read_data()
    except json.JSONDecodeError:
        print("Error reading JSON data.")
        return {
            "favourite_teams": [],
            "match_notes": [],
            "generated_summaries": []
        }
def save_data(data):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print("Error saving data:", e)
def save_favourite_team(team):
    data = read_data()
    if team not in data["favourite_teams"]:
        data["favourite_teams"].append(team)
        save_data(data)
def load_favourite_teams():
    data = read_data()
    return data["favourite_teams"]
def save_match_note(note):
    data = read_data()
    data["match_notes"].append(note)
    save_data(data)
def load_match_notes():
    data = read_data()
    return data["match_notes"]
def save_generated_summary(summary):
    data = read_data()
    data["generated_summaries"].append(summary)
    save_data(data)
initialize_file()
